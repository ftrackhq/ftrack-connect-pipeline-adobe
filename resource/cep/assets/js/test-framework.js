//window.alert("Creating session");
//console.log('Creating session');
document.write("Creating session...<br>");
var session = new ftrack.Session(
    'https://ftrack-integrations.ftrackapp.com',
    'henrik.norin@ftrack.com',
    'YWNkMTJjY2ItMmYzYy00ZmJjLWI3NWMtNDdiMWFiZWFkMmQxOjo0ZTQ1MDEyNy1hM2QzLTRkMDEtYWQ5NS02ZGNjN2E4MWE0ZWU', 
    { autoConnectEventHub: true }
);


//var adobe_id = 'f2140d35-30c6-42e8-b211-642338cdbb79';
var adobe_id = '1234';

var event = new ftrack.Event('ftrack.pipeline.client.launch', {
    pipeline: {
    	app_id: adobe_id,
    	name: 'publisher',
   		source: ''
    }
})
document.write("Publishing event: "+JSON.stringify(event)+"<br>");
session.eventHub.publish(event)
