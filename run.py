from app import server, app_dash, mongo
from werkzeug.serving import run_simple
#from werkzeug.middleware.dispatcher import DispatcherMiddleware
#from werkzeug.wsgi import DispatcherMiddleware


#app = DispatcherMiddleware( server, {
#    '/dash': app_dash.server
#})

if __name__=='__main__':
	#J'avais pas la premiere ligne avant
	run_simple('0.0.0.0', 5000, server, use_reloader=True, use_debugger=True) #essayer juste avec ca 
	#app_dash.run_server(host='0.0.0.0', port=5000, debug=True)

	#run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)