import API_operations
import Bitbay
import Bittrex
import Wallet
import Alpha_vantage
import Raport
import Eod

# This file is only for testing, every functionality is in GUI

def main():
    eod = Eod.Eodhistoricaldata()
    print(eod.request_market_data())


if __name__ == "__main__":
    main()
