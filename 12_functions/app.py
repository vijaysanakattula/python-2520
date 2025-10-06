# search by skill ==> loop & condition (filter)
def search_students():
    skill_to_search = input("Enter Skill To Search: ")
    filtered_students = list(filter(lambda s: skill_to_search in students[s]['skills'], students))
    print(filtered_students)
    