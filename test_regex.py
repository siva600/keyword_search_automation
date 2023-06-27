
import re
cmd = data['plugin']['params']['instset'][0]['cmd']
inst = data['plugin']['params']['instset'][0]['inst']
host = data['plugin']['params']['instset'][0]['host']
object = data['plugin']['params']['instset'][0]['object']
values = tuple(re.findall(r'-(?:c|t|l|i|u|s)\s+"?(.*?)"?\s', cmd))
plugin_data = data.get('plugin')
values = tuple(value.strip('"') for value in values)

print(values)

required_data = {"plugin": {"params": {"instset": [{"object":object.strip('"'),
                                           "cmd": "-c {} -t \"{}\" -l \"{}\" -i \"{}\" -u {} -s {}".format(values[0], values[1], values[2], values[3], values[4], plugin_data.get('timestamp')),
                                           "inst": inst, "host": "'{}'".format(host)}]}, "group": plugin_data.get('group'),
                   "timestamp": plugin_data.get('timestamp'), "mode": plugin_data.get('mode'), "requestor": plugin_data.get('requestor'), "type": plugin_data.get('type'),
                   "id": plugin_data.get('em_plugin'), "node": plugin_data.get('node'), "instance": plugin_data.get('instance'), "grouptype": plugin_data.get('grouptype')}}

print(required_data)

