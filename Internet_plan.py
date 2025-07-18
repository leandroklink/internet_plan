class DataTier:
    def __init__(self, min, max, price_per_gb):
        self.min = min
        self.max = max
        self.price_per_gb = price_per_gb

class InternetPlan:
    def __init__(self, provider, name, data_usages, monthly_fee):
        self.provider = provider
        self.name = name
        self.data_usages = data_usages
        self.monthly_fee = monthly_fee
        self.cost = None

    def calc_cost(self, data_usage):
        cost = 0
        if self.data_usages:
            for tier in self.data_usages:
                if(tier.min is None or data_usage > tier.min) and (tier.max is None or data_usage <= tier.max):
                    cost += data_usage * tier.price_per_gb
                    break
        if self.monthly_fee:
            cost+=self.monthly_fee  

        self.cost = cost
        return cost
    
NetMax = InternetPlan(
    provider = "Leandro's Net",
    name = "NetMax",
    data_usages=[
        DataTier(min=None, max=80, price_per_gb=5),
        DataTier(min=80, max=120, price_per_gb=15),
        DataTier(min=120, max=180, price_per_gb=20),
        DataTier(min=180, max=None, price_per_gb=30)
        ],
    monthly_fee=30
)


MegaNet = InternetPlan(
    provider = "OMG Net",
    name = "MegaNet",
    data_usages=[
        DataTier(min=None, max=80, price_per_gb=10),
        DataTier(min=80, max=120, price_per_gb=15),
        DataTier(min=120, max=180, price_per_gb=18),
        DataTier(min=180, max=None, price_per_gb=25)
        ],
    monthly_fee=40
)

NetUltra = InternetPlan(
    provider = "HareverNet",
    name = "NetUltra",
    data_usages=[
        DataTier(min=None, max=80, price_per_gb=15),
        DataTier(min=80, max=120, price_per_gb=25),
        DataTier(min=120, max=180, price_per_gb=35 ),
        DataTier(min=180, max=None, price_per_gb=45)
        ],
    monthly_fee=25
)


data_usage = float(input("Enter your data usage to calculate how internet plan its cheapest for you: "))


plans = [NetMax, MegaNet, NetUltra]

sorted_plans = sorted(plans, key=lambda plan: plan.calc_cost(data_usage))
cheap = sorted_plans[0]


print(f"* Most cheapest Plan for a {data_usage} of data usage:")
print("~~~~"*3)
print(f"* Providor: {cheap.provider}")
print(f"* Name: {cheap.name}")
print(f"* Total Cost: {cheap.cost:.2f}")
print()