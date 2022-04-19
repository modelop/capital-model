

# modelop.init
def init():
    print("Model Initialization")


# modelop.score
def action(data):
    print("Do your scoring here")
    yield data


# modelop.metrics
def metrics(data):
    print("Do any built in metrics reporting here")
    yield {"foo": 1}

