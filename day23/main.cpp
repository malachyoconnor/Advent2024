#include <array>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

string get_chars(int input) {
  return string(1, input >> 8) + string(1, input & 0xFF);
}

unordered_map<int, unordered_set<int>> neighbour_map;


std::pair<int, string> count_nodes_that_involve_us(int me, vector<int> original_partygoers, unordered_set<int> visited) {

  visited.insert(me);
  original_partygoers.push_back(me);

  int max_new = 1;
  string max_string = get_chars(me);

  for (auto neighbour : neighbour_map[me]) {

    if (visited.count(neighbour) > 0) {
      continue;
    }

    // If all the original partygoers have a connection to you
    bool can_add = true;
    for (int original_partygoer : original_partygoers) {
      if (neighbour_map[original_partygoer].count(neighbour) == 0) {
        can_add = false;
        break;
      }
    }

    if (can_add) {
      auto [test_max, test_string] = count_nodes_that_involve_us(neighbour, original_partygoers, visited);
      test_max += 1;
      if (test_max > max_new) {
        max_new = test_max;
        max_string = get_chars(me) + test_string;
      }
    }
    visited.insert(neighbour);
  }

  return {max_new, max_string};
}

int main() {

  char c1, c2, c3, c4;
  char dash;
  freopen("input.txt", "r", stdin);

  while (cin >> c1 >> c2 >> dash >> c3 >> c4) {

    int player1 = (c1 << 8) | c2;
    int player2 = (c3 << 8) | c4;

    if (neighbour_map.count(player1) > 0) {
      neighbour_map[player1].insert(player2);
    } else {
      neighbour_map[player1] = unordered_set<int>{player2};
    }

    if (neighbour_map.count(player2) > 0) {
      neighbour_map[player2].insert(player1);
    } else {
      neighbour_map[player2] = unordered_set<int>{player1};
    }
  }

  int total_count = 0;
  int t_count = 0;

  for (auto &[me, neighbours] : neighbour_map) {

    for (auto neighbour : neighbours) {
      if (not(me < neighbour)) continue;
      auto grand_neighbours = neighbour_map[neighbour];

      for (auto grand_neighbour : grand_neighbours) {
        if (not(neighbour < grand_neighbour)) continue;
        if (neighbours.count(grand_neighbour)) {
          total_count++;

          if ((me >> 8) == 't' or (neighbour >> 8) == 't' or (grand_neighbour >> 8) == 't') {
            t_count++;
          }
        }
      }
    }
  }
  cout << "Total 't' neighbours: " << t_count << endl;

  int max_size = 0;
  string max_string;
  for (const auto& [node, value] : neighbour_map) {
    auto [found_max, found_max_string] = count_nodes_that_involve_us(node, vector<int>{}, unordered_set<int>{});

    if (found_max > max_size) {
      max_string = found_max_string;
      max_size = found_max;
    }
  }
  
  vector<std::string> names;

  for (int i = 0; i < (int) max_string.length(); i += 2) {
    
    cout << max_string.substr(i, 2) << endl;

    names.push_back(max_string.substr(i, 2));
  }

  std::sort(names.begin(), names.end());

  cout << "Solution 2";
  for (auto name : names) {
    cout << name << ",";
  }

}

// by ie zb am mr sn mt gf yi aq ge te rw