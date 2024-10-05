def probThree():
    people = {'users':
              {
               'John': 19,
               'Emily': 21,
               'Sarah': 25,
               'Tom': 18
              }
             }
    print('User/s that is older than 19\n')
    for _, inner in people.items():
        for user, age in inner.items():
            if age > 19:
                print(f'Name: {user}')
