#include <iostream>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <unordered_map>
using namespace std;

long long mix(long long secret, long long other) {
    return secret ^ other;
}


long long prune(long long secret) {
	return secret % 16777216LL;
}

int get_price(long long secret) {
	return secret % 10;
}

std::unordered_map<long long, long long> secret_memoizer;

long long next_secret(long long secret) {
	if (secret_memoizer.count(secret) != 0) {
		return secret_memoizer.at(secret);
	}

	long long initial_secret = secret;

	secret = mix(secret, secret << 6);
    secret = prune(secret);

    secret = mix(secret, secret / 32LL);
    secret = prune(secret);

    secret = mix(secret, secret << 11);
    secret = prune(secret);

	secret_memoizer[initial_secret] = secret;

    return secret;
}

void update_sequence(std::vector<int8_t>& price_sequence, int price_change) {
	if (price_sequence.size() < 4) {
		price_sequence.push_back(price_change);
		return;
	}

	price_sequence[0] = price_sequence[1];
	price_sequence[1] = price_sequence[2];
	price_sequence[2] = price_sequence[3];
	price_sequence[3] = price_change;
}

typedef long long TUPLE;
std::vector<std::map<TUPLE, int>> monkey_sequences;

void update_stored_best_sequences(const std::vector<int8_t>& sequence, int monkey_id, int price) {
	if (sequence.size() < 4) {
		return;
	}

	long long element0 = ((int) ((1<<8) - 1) & sequence[0]);
	long long element1 = ((int) ((1<<8) - 1) & sequence[1]);
	long long element2 = ((int) ((1<<8) - 1) & sequence[2]);
	long long element3 = ((int) ((1<<8) - 1) & sequence[3]);
	
	TUPLE seq_tup = (element0 << 48) | (element1 << 32) | (element2 << 16) | element3;

	if (monkey_sequences[monkey_id].count(seq_tup) > 0) {
		return;
	}

	monkey_sequences[monkey_id][seq_tup] = price;
}

int main() {

	FILE* success = freopen("input.txt", "r", stdin);
	assert(success != 0);

	std::vector<long long> secrets;
	int n;
	while (cin >> n) {
		secrets.push_back(n);
	}

	int monkey_id = 0;
	for (auto secret : secrets) {

		int prev_price = get_price(secret);
		std::vector<int8_t> price_change_sequence;
		monkey_sequences.push_back({});

		for (int i = 0; i < 2000; i++) {
			secret = next_secret(secret);
			int new_price = get_price(secret);

			int price_change = new_price - prev_price;
			update_sequence(price_change_sequence, price_change);
			update_stored_best_sequences(price_change_sequence, monkey_id, new_price);

			prev_price = new_price;
		}

		monkey_id += 1;
	}

	cout << "STARTING NEXT ITERATION" << endl;

	std::set<TUPLE> all_sequences;

	for (const auto& sequence_dict : monkey_sequences) {
		
		for (auto [key, value]: sequence_dict) {
			all_sequences.insert(key);
		}
	}
	
	int best_price = 0;
	for (TUPLE sequence_tup: all_sequences) {

		cout << best_price << "\r";

		int total = 0;

		for (const auto& sequence_dict: monkey_sequences) {
			total = total + (sequence_dict.count(sequence_tup) > 0 ? sequence_dict.at(sequence_tup) : 0);
		}

		best_price = max(best_price, total);
	}

	cout << best_price << endl;

	return 0;
}