import openalpr_api
import os

apiclient = openalpr_api.DefaultApi()
key = os.environ.get('OPENALPR_SECRET_KEY', "sk_DEMODEMODEMODEMODEMODEMO")
print("Using key: %s" % key)

response = apiclient.recognize_post(key, "plate,color,make,makemodel", image="C:\Users\Panda\Documents\GitHub\Garage-Automation\License Plate Reader\openalpr\samples\us-3.jpg", country="us")


# print dir(response.plate.to_dict())
# plate = response.plate.to_dict()
# for k, v in plate.iteritems():
# 	print "%s : %s" % (k, v)

# for res in plate['results']:
# 	print "Plate:      %s - %f percent" % (res.plate, res.confidence)


# print "Plate:      %s - %f percent" % (response.plate.results[0].plate, response.plate.results[0].confidence)
# print "Color:      %s - %f percent" % (response.color[0].value, response.color[0].confidence)
# print "Make:       %s - %f percent" % (response.make[0].value, response.make[0].confidence)
# print "Make-model: %s - %f percent" % (response.makemodel[0].value, response.makemodel[0].confidence)


for plate_obj in response.plate.results:
    print "Plate:      %s - %f percent" % (plate_obj.plate, plate_obj.confidence)

print "Color:      %s - %f percent" % (response.color[0].value, response.color[0].confidence)
print "Make:       %s - %f percent" % (response.make[0].value, response.make[0].confidence)
print "Make-model: %s - %f percent" % (response.makemodel[0].value, response.makemodel[0].confidence)
