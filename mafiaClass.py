
class Mafia:

    def __init__(self, name, num_of_crooks, crooks_power, money,
                 territory, mafia_number):
        self.name = name
        self.num_of_crooks = num_of_crooks
        self.crooks_power = crooks_power
        self.money = money
        self.territory = territory
        self.crooks_cost_per_number_yearly = 155 * self.num_of_crooks
        self.crooks_cost_per_power_yearly = 120 * self.crooks_power
        self.total_expenses_per_crook_yearly = self.crooks_cost_per_number_yearly + \
                                               self.crooks_cost_per_power_yearly
        self.is_player = False
        self.is_eliminated = False
        self.mafia_number = mafia_number
        self.total_power = num_of_crooks * crooks_power

    # Takes in a string and returns an operator in form of a string to use in an expression
    @staticmethod
    def define_operation(string):
        if string.casefold() == "multiply" \
                or string == "*" \
                or string.casefold() == "x" \
                or string.casefold() == "mult":
            return " * "
        if string.casefold() == "add" \
                or string == "+" \
                or string.casefold() == "addition":
            return " + "
        if string.casefold() == "divide" \
                or string == "/" \
                or string.casefold() == "dev":
            return " / "
        if string.casefold() == "subtract" \
                or string == "-" \
                or string.casefold() == "sub":
            return " - "

    # takes in a string and returns an attribute name that resembles that string
    @staticmethod
    def define_stat(string):
        if string.casefold() == "name":
            return "name"
        if string.casefold() == "crooks":
            return "num_of_crooks"
        if string.casefold() == "power":
            "crooks_power"
        if string.casefold() == "money":
            return "money"
        if string.casefold() == "territory":
            return "territory"
        if string.casefold() == "crooks cost":
            return "crooks_cost_per_number_yearly"
        if string.casefold() == "power cost":
            return "crooks_cost_per_power_yearly"
        if string.casefold() == "total cost":
            return "total_expenses_per_crook_yearly"
        if string.casefold() == "player":
            return "is_player"
        if string.casefold() == "eliminated":
            return "is_eliminated"
        if string.casefold() == "number" or string.casefold() == "mafia number":
            return "mafia_number"
        if string.casefold() == "total power":
            return "total_power"

    @staticmethod
    def create_expression(number1, operation, number2):
        expression = str(number1) + Mafia.define_operation(operation) + str(number2)
        return expression

    # Uses define_stat to figure out what attribute will be changed
    # Uses define_operation to figure out the operation that has to be done on the figured out attribute
    # Creates the expression in form of a string that is evaluated, the result will be set as the new
    # Value of the same attribute that has been taken for the operation
    def change_stat(self, number, stat_to_change, operation):
        stat = Mafia.define_stat(stat_to_change)
        value_stat = getattr(self, stat)
        expression = Mafia.create_expression(value_stat, operation, number)
        setattr(self, Mafia.define_stat(stat_to_change), eval(expression))
        stat = Mafia.define_stat(stat_to_change)
        return getattr(self, stat)

    def send_crooks_to_war(self, number):
        self.change_stat(number, "crooks", "subtract")
        return number

    def update_total_power(self):
        self.total_power = self.num_of_crooks * self.crooks_power

    def update_costs(self):
        self.crooks_cost_per_number_yearly = 155 * self.num_of_crooks
        self.crooks_cost_per_power_yearly = 120 * self.crooks_power
        self.total_expenses_per_crook_yearly = self.crooks_cost_per_number_yearly + \
                                               self.crooks_cost_per_power_yearly

    def cost_processing(self):
        self.update_costs()
        self.change_stat(self.total_expenses_per_crook_yearly, "money", "subtract")

    def increase_crooks_numbers_yearly_rate(self):
        from main import make_random_zero35
        stat_increase = make_random_zero35() * self.num_of_crooks
        self.change_stat(stat_increase, "crooks", "add")

    def increase_crooks_power_yearly_rate(self):
        from main import random_number_with_external_variable
        stat_increase = random_number_with_external_variable(self.territory) + self.crooks_power
        self.change_stat(stat_increase, "power", "add")

    # using formula_money_gain from main, applies the money growth(or loss) formula as if an in-game year has passed
    def increase_money_yearly_rate(self):
        from main import formula_money_gain
        stat_increase = formula_money_gain(self.territory)
        self.change_stat(stat_increase, "money", "add")

    # applies the "yearly rates"; in other words: applies the changes that happen in an in-game year
    def comprehensive_yearly_process(self):
        self.increase_money_yearly_rate()
        self.increase_crooks_numbers_yearly_rate()
        self.increase_crooks_power_yearly_rate()
        self.update_total_power()
        self.cost_processing()

    # print full details as a class function. eg: Mafia.full_details
    def full_details(self):
        return \
            "Info. Name: {}. \n" \
            "Number Of Crooks: {}. \n" \
            "Power Per Crook: {}. \n" \
            "Current Cash: {}. \n" \
            "Territory: {}. \n" \
            "Player? {}. \n" \
            "Eliminated? {}. \n" \
            "Mafia number: {}. \n" \
            "Total Power: {}. \n".format(self.name,
                                         self.num_of_crooks,
                                         self.crooks_power,
                                         self.money,
                                         self.territory,
                                         self.is_player,
                                         self.is_eliminated,
                                         self.mafia_number,
                                         self.total_power)
