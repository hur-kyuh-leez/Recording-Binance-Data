"""Script to gather 10-sec market data from Binance"""
from pytz import utc
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import csv
import binance
from PRIVATE_INFO import public_api, secret_api


# setting  public api and secret api keys
binance.set(public_api, secret_api)

# not really using this code
def time_this_code(timethiscode):
    """simply calculating execution time"""
    import timeit
    start = timeit.default_timer()
    timethiscode
    end = timeit.default_timer()
    return (end - start)

def write_price():
    """writing prices to csv files"""
    data = binance.prices()     # calling prices
    print(int(time.time() * 1000))
    print(data)
    for each_market in data:
        # outputs "binance time" in miliseconds
        write_price.time_index = int(time.time() * 1000)
        current_price = float(data['%s' % each_market])
        with open('./csv_data/%s.csv' % each_market, 'a') as f:
            wr = csv.writer(f)
            wr.writerow([write_price.time_index, current_price])


def main():
    """Run tick() at the interval of every ten seconds."""
    scheduler = BlockingScheduler(timezone=utc)
    scheduler.add_job(write_price, 'interval', seconds=10, max_instances=3)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass



if __name__ == '__main__':
    main()
