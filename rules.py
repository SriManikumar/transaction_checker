def check_duplicates(transactions):
    seen = set()
    return [txn.transaction_id for txn in transactions if txn.transaction_id in seen or seen.add(txn.transaction_id)]

def check_currency(transactions, valid_currencies):
    return [txn.transaction_id for txn in transactions if txn.currency not in valid_currencies]

def check_timestamp_order(transactions):
    sorted_txns = sorted(transactions, key=lambda x: x.timestamp)
    return all(sorted_txns[i].timestamp <= sorted_txns[i+1].timestamp for i in range(len(sorted_txns)-1))
