from matplotlib import pyplot as plt  
import algorithms as alg


def plot_time_graph(algorithm):
    iterations = alg.get_int(10, 10000, "How many times you want to execute your algorithm?: ")
    max_size = alg.get_int(200, 500, "Maximum stomach capacity: ")
    min_size = alg.get_int(100, 150, "Minimum stomach capaity: ")
    how_many = alg.get_int(20, 120, "How many donuts you want to generate? : ")
    params = alg.gather_information(algorithm, 
                                    max_size, min_size, how_many, iterations)
    results, stomach_sizes = params

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.style.use('ggplot')
    title = "Time of executing " + algorithm + " algorithm "
    title += str(iterations) + " times"
    plt.title(title, fontsize=24)
    plt.xlabel("Stomach capacity", fontsize=16)
    plt.ylabel("Time in seconds", fontsize=16)
    plt.plot(stomach_sizes, results, c='purple')
    plt.savefig(title, bbox_inches='tight')


plot_time_graph("recursive")