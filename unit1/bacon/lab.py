import json

def make_actor_dictionary(data):
    actors = {}
    for actor_pair in data:
        actor_0 = actor_pair[0]
        actor_1 = actor_pair[1]
        if actor_0 not in actors:
            actors[actor_0] = []
        if actor_1 not in actors:
            actors[actor_1] = []
        actors[actor_0].append(actor_1)
        actors[actor_1].append(actor_0)
    return actors

def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    actor_dict = make_actor_dictionary(data)
    return (actor_id_1 in actor_dict[actor_id_2])

def get_actors_with_bacon_number(data, n):
    actor_dict = make_actor_dictionary(data)
    visited = set()
    q = [(4724, 0)]
    result = set()
    while q:
        current_actor, number = q.pop(0)
        if current_actor not in visited:
            visited.add(current_actor)

            if number == n:
                result.add(current_actor)
                continue
            for co_star in actor_dict[current_actor]:
                q.append((co_star, number + 1))
    
    return result



def get_bacon_path(data, actor_id):
    

def get_path(data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")

def actor_path(data, path):
    raise NotImplementedError("Implement me!")

def get_movie_path(data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")

if __name__ == '__main__':
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    pass
