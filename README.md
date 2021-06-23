# pele_client
REST-based class for issuing Pele requests (HySDS Datasets API)

### Installation
First, gdal (osgeo) must be installed via conda using the conda-forge channel:
```
conda install -c requirements.txt.forge
```
then the client is installed:
``` 
python setup.py install
```

### Examples
To have the requests client automatically renew the client session upon expiration, ensure your login creds are set in your .netrc file, e.g.
```
bash
cat ~/.netrc
# machine localhost login koa@test.com password test
# macdef init


```
The Pele requests client will then use your creds to attain an API token to use for subsequent API calls. When the token expires, the client will refresh the token automatically:
```
python
from pele_client.client import PeleRequests

base_url = "http://localhost:8877/api/v0.1"

# instantiate PeleRequests object
pr = PeleRequests(base_url)

# now use like requests module (`request()`, `get()`, `head()`, `post()`, `put()`, `delete()`, `patch()`)
r = pr.get(base_url + '/test/echo', params={'echo_str': 'hello world'})

```
The utility function ```getPeleExtentFromOGRFile``` extracts the bounding box encompassing the layer/features in the given OGR-compliant file. If the file is multi-layer, an
optional layer name can be specified, otherwise the first/top layer is used by default. The format of the returned extent is compatible with Pele geospatial searches.
```
from pele_client.client import PeleRequests, getPeleExtentFromOGRFile

pr = PeleRequests('https://100.64.122.98/pele/api/v0.1', verify=False)

extent = getPeleExtentFromOGRFile('/home/wasabi/ucayali_boundary.geojson', 'ucayali_boundary')

response = pr.post(base_url + '/pele/dataset/L2_L_GSLC/dataset_ids', json = { 'polygon' : extent })
response_json = response.json()

datasets = ressponse_json['dataset_ids']
```
