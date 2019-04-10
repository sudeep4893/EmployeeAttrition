import tableauserverclient as TSC
"""
tableau_auth = TSC.TableauAuth('sudeep48raj93@gmail.com', 'August$4893')
server = TSC.Server('http://public.tableau.com')

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])
"""

tableau_auth = TSC.TableauAuth('sudeep48raj93@gmail.com', 'August$4893')
server = TSC.Server('https://online.tableau.com/')

with server.auth.sign_in(tableau_auth):
    pass
print('connection made')

server.auth.sign_out()
print('connection closed')