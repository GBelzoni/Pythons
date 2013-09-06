from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

import json




def index(request):
    
    #Get data
    path = '/home/phcostello/Documents/workspace/TestD3JS'
    fin = open( path + '/flare.json')
    data = fin.read()
    json_data = json.loads(data,encoding='utf-8')
    json_str = json.dumps(json_data)
    fin.close()
    
    t = loader.get_template('TestD3JS/index.html')
    c = Context({'json_str':json_str})
    print json_str
    
    return HttpResponse(t.render(c))
