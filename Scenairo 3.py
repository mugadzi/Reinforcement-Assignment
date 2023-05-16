from FourRooms import FourRooms
import numpy as np


def main():

    var = input(
        "Welcome \n Would you like to run this in a stochastic simulation?\n Y or N\n ")

    if var == 'Y':
        stochastic = True
    else:
        stochastic = False

    # Create the FourRooms Object
    fourRoomsObj = FourRooms('rgb', stochastic)
    # set learning  and discount rate
    gamma = 0.7
    epsilon = 0.7
    n = 0.8

    # initialize the tables (Q and R) in three dimentions
    rewards = np.full((13, 13), (-1)), np.full((13, 13),
                                               (-1)), np.full((13, 13), (-1))
    q_table = np.zeros((13, 13, 4)), np.zeros(
        (13, 13, 4)), np.zeros((13, 13, 4))

    isTerminal = False
    fourRoomsObj

    for epochs in range(7000):
        fourRoomsObj.newEpoch()
        # Initialize the first package
        firstpack = fourRoomsObj.RED
        # get new starting position for new epoch
        position = fourRoomsObj.getPosition()
        while not isTerminal:
            # Perform action using greedy algorithm
            action = greedyAlogrithm(position, epsilon, q_table)

            # Perform the action and collect return values
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(
                action)
            firstpack -= 1
            # Rewards system
            if gridType == firstpack:

                rewards[firstpack][newPos] = 100
            elif gridType == 0:

                rewards[firstpack][newPos] = -1
            else:

                rewards[firstpack][newPos] = -50
                if gridType > 0:
                    isTerminal = Ture

            list(q_table)[firstpack] = (q_generator(position, newPos, action,
                                                    rewards[firstpack], q_table[firstpack], n, gamma))
            position = newPos

        isTerminal = False
        if inCol:
            firstpack = + 1
            inCol = False

        if packagesRemaining == 0:
            continue

        isTerminal = False

    print(q_table)
    print(rewards)
    fourRoomsObj.showPath(-1)


def greedyAlogrithm(position, epsilon, q_table):
    # if a randomly chosen value between 0 and 1 is less than epsilon,
    # choose the most promising value from the Q-table for this state.
    if np.random.random() < epsilon:
        return np.argmax(q_table[position])
    else:
        return np.random.randint(4)

# Updates the Q table using the formula


def q_generator(position, newPos, action, rewards, q_table, n, gamma):
    reward = rewards[newPos]
    prevQ = q_table[position[0]][position[1]][action]
    temporalDifference = reward + (gamma * np.max(q_table[newPos])) - prevQ
    q_table[position[0]][position[1]][action] = prevQ + n * temporalDifference

    return q_table


if __name__ == "__main__":
    main()