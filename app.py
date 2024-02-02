import mirror

dashboard = mirror.Mirror(__name__, "config.yml")

if __name__ == '__main__':
    dashboard.run()
