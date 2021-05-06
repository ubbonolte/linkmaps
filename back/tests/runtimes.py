from graph_service import WikiGraphGenerator
import timeit

def run_wiki_generator():
    generator = WikiGraphGenerator()

    start = timeit.default_timer()
    graph = generator.generate('Cook_(domestic_worker)', depth=1)
    stop = timeit.default_timer()
    print ("Cook_(domestic_worker), Depth == 1: Runtime = ", stop - start, "s, Graph = ", graph)

    start = timeit.default_timer()
    graph = generator.generate('Cook_(domestic_worker)', depth=2)
    stop = timeit.default_timer()
    print ("Cook_(domestic_worker), Depth == 2: Runtime = ", stop - start, "s, Graph = ", graph)

    start = timeit.default_timer()
    graph = generator.generate('Albert Einstein', depth=1)
    stop = timeit.default_timer()
    print ("Albert Einstein, Depth == 1: Runtime = ", stop - start, "s, Graph = ", graph)

    start = timeit.default_timer()
    graph = generator.generate('Albert Einstein', depth=2)
    stop = timeit.default_timer()
    print ("Albert Einstein, Depth == 2: Runtime = ", stop - start, "s, Graph = ", graph)

run_wiki_generator()