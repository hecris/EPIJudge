from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # TODO - you fill in here.
    dp = [[0 for _ in range(len(individual_play_scores))] for _ in range(final_score+1)]

    for j in range(len(individual_play_scores)):
        dp[0][j] = 1

    for i in range(1,final_score+1):
        for j in range(len(individual_play_scores)):
            coin = individual_play_scores[j]
            with_coin = dp[i-coin][j] if i - coin >= 0 else 0
            without_coin = dp[i][j-1] if j >= 1 else 0
            dp[i][j] = with_coin + without_coin

    return dp[final_score][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
