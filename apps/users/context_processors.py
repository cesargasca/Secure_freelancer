def add_variable_to_context(request):
    type_of_user = 'n'
    if  not request.user.is_anonymous:
        type_of_user = request.user.type_of_user
    print(type_of_user)
    return {
        'testme': 'Hello world!',
        'type_of_user': type_of_user
    }