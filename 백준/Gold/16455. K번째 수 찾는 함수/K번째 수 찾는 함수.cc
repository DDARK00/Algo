#include <algorithm>
#include <vector>
#include <random>

int kth(std::vector<int> &a, int k) {
    static std::mt19937 g(std::random_device{}());
    std::shuffle(a.begin(), a.end(), g);
	std::nth_element(a.begin(), a.begin() + k-1, a.end());
	return a[k - 1];
}