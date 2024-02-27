import cProfile
import pstats

def pytest_runtest_call(item):
    profiler = cProfile.Profile()
    profiler.enable()
    item.runtest()
    profiler.disable()
    ps = pstats.Stats(profiler).sort_stats('cumulative')
    print(f"Profile for {item.name}")
    ps.print_stats()
