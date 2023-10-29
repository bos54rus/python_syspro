def format_table(benchmarks, algos, results):
    columns_width_list = [max(len("Benchmark"), max([len(i) for i in benchmarks]))]
    for n in range(len(algos)):
        columns_width_list.append(max(len(algos[n]), max([len(str(results[j][n])) for j in range(len(results))])))

    first_row = f"| {'Benchmark'.ljust(columns_width_list[0])} |"
    for i in range(len(algos)):
        first_row += f" {algos[i].ljust(columns_width_list[i + 1])} |"
    print(first_row)

    sum_width = sum(columns_width_list) + 3 * len(algos) + 2
    print("|", "-" * sum_width, "|", sep="")

    for i in range(len(benchmarks)):
        line = f"| {benchmarks[i].ljust(columns_width_list[0])} |"
        for j in range(len(results[i])):
            line += f" {str(results[i][j]).ljust(columns_width_list[j + 1])} |"
        print(line)


format_table(["best case", "worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])