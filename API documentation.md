Title: Rest API Documentation

URL Source: https://ontox.elixir-luxembourg.org/minerva/docs/index.html

Markdown Content:
1\. Introduction
----------------

For API calls that require authentication MINERVA\_AUTH\_TOKEN obtained during login process must be included.

2\. QuickStart guide
--------------------

Here is sample example that shows information about all projects accessible by guest account (anonymous user):

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/' -X GET
```

If we are interested in the API calls that require more privileges than anonymous user we need to login first:

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/doLogin' -X POST \
    -d 'login=admin&password=admin' \
    -H 'Content-Type: application/x-www-form-urlencoded'
```

```
{
  "info" : "Login successful.",
  "login" : "admin",
  "token" : "45197"
}
```

The response creates an authentication token and puts it into a cookie MINERVA\_AUTH\_TOKEN=xxxxxxxx. When using console curl command this cookie must be attached to every query that follows. When we have authentication token we can access information about specific user on the server:

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
```

3\. Categories
--------------

### 3.1. [Authentication](https://ontox.elixir-luxembourg.org/minerva/docs/authentication.html)

### 3.2. [Configuration](https://ontox.elixir-luxembourg.org/minerva/docs/configuration.html)

Methods allowing to obtain configuration information from server and updating it with proper privileges

### 3.3. [Converter](https://ontox.elixir-luxembourg.org/minerva/docs/converter.html)

Conversion API provides access to MINERVA’s ability to convert between different systems biology network formats and to export of layouts to different graphical formats

### 3.4. [Files](https://ontox.elixir-luxembourg.org/minerva/docs/file.html)

Methods that allow to upload files into the system

### 3.5. [Genomics](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html)

Methods allowing to access genome data

### 3.6. [License](https://ontox.elixir-luxembourg.org/minerva/docs/license.html)

Methods allowing to access information about available licenses

### 3.7. [Mesh](https://ontox.elixir-luxembourg.org/minerva/docs/mesh.html)

Methods allowing to access info about mesh data

### 3.8. [Plugins](https://ontox.elixir-luxembourg.org/minerva/docs/plugin.html)

Methods allowing to store some data for plugin infrastructure

### 3.9. [Project](https://ontox.elixir-luxembourg.org/minerva/docs/project.html)

Set of methods allowing to obtain information about projects and allowing to create new project and modifying existing ones

### 3.10. [Taxonomy](https://ontox.elixir-luxembourg.org/minerva/docs/taxonomy.html)

Methods allowing to access info about taxonomy data

### 3.11. [Users](https://ontox.elixir-luxembourg.org/minerva/docs/user.html)

Set of methods allowing to obtain and manage users and their access control

Title: Rest API Documentation - Authentication

URL Source: https://ontox.elixir-luxembourg.org/minerva/docs/authentication.html

Markdown Content:
1\. Login
---------

Login to the system. If credentials are invalid response with 403 status code will be returned. Token will be valid for the next 120 minutes.

### 1.1. CURL sample

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/doLogin' -X POST \
    -d 'login=admin&password=admin' \
    -H 'Content-Type: application/x-www-form-urlencoded'
```

### 1.2. Request Parameters

 
| Parameter | Description |
| --- | --- |
| `login`
 | login

 |
| `password`

 | password

 |

### 1.3. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `info`
 | `String`

 | status message

 |
| `login`

 | `String`

 | user login

 |
| `token`

 | `String`

 | session token

 |

### 1.4. Sample Response

```
{
  "info" : "Login successful.",
  "login" : "admin",
  "token" : "45197"
}
```

2\. Logout
----------

Logout from the system.

### 2.1. CURL sample

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/doLogout' -X POST \
    --cookie 'MINERVA_AUTH_TOKEN=xxxxxxxx' \
    -H 'Content-Type: application/x-www-form-urlencoded'
```

### 2.2. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `status`
 | `String`

 | status message

 |

### 2.3. Sample Response

```
{
  "status" : "OK"
}
```

3\. Check if session is still valid
-----------------------------------

Sometimes there is need for verification if user is authenticated in the current session (for instance we might need this information to check if our session did not expire). This API call returns information if the session is still valid.

### 3.1. CURL sample

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/isSessionValid' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
```

### 3.2. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `login`
 | `String`

 | user login of the session owner

 |

### 3.3. Sample Response

```
{
  "login" : "admin"
}
```


Title: Rest API Documentation - Configuration

URL Source: https://ontox.elixir-luxembourg.org/minerva/docs/configuration.html

Markdown Content:
```
{
  "options" : [ {
    "idObject" : 4,
    "type" : "DEFAULT_MAP",
    "valueType" : "STRING",
    "commonName" : "Default Project Id",
    "isServerSide" : false,
    "value" : "empty",
    "group" : "Server configuration"
  }, {
    "idObject" : 14,
    "type" : "LEFT_LOGO_IMG",
    "valueType" : "URL",
    "commonName" : "Left logo icon",
    "isServerSide" : false,
    "value" : "resources/images/udl.png",
    "group" : "Legend and logo"
  }, {
    "idObject" : 15,
    "type" : "LEFT_LOGO_LINK",
    "valueType" : "URL",
    "commonName" : "Left logo link (after click)",
    "isServerSide" : false,
    "value" : "https://wwwen.uni.lu/",
    "group" : "Legend and logo"
  }, {
    "idObject" : 16,
    "type" : "LEFT_LOGO_TEXT",
    "valueType" : "STRING",
    "commonName" : "Left logo description",
    "isServerSide" : false,
    "value" : "University of Luxembourg",
    "group" : "Legend and logo"
  }, {
    "idObject" : 17,
    "type" : "RIGHT_LOGO_IMG",
    "valueType" : "URL",
    "commonName" : "Right logo icon",
    "isServerSide" : false,
    "value" : "resources/images/lcsb.png",
    "group" : "Legend and logo"
  }, {
    "idObject" : 18,
    "type" : "RIGHT_LOGO_LINK",
    "valueType" : "URL",
    "commonName" : "Right logo link (after click)",
    "isServerSide" : false,
    "value" : "https://wwwen.uni.lu/lcsb/",
    "group" : "Legend and logo"
  }, {
    "idObject" : 19,
    "type" : "RIGHT_LOGO_TEXT",
    "valueType" : "STRING",
    "commonName" : "Right logo description",
    "isServerSide" : false,
    "value" : "LCSB - Luxembourg Centre for Systems Biomedicine",
    "group" : "Legend and logo"
  }, {
    "idObject" : 20,
    "type" : "SEARCH_DISTANCE",
    "valueType" : "DOUBLE",
    "commonName" : "Max distance for clicking on element (px)",
    "isServerSide" : false,
    "value" : "10",
    "group" : "Point and click"
  }, {
    "idObject" : 21,
    "type" : "REQUEST_ACCOUNT_EMAIL",
    "valueType" : "EMAIL",
    "commonName" : "Email used for requesting an account",
    "isServerSide" : false,
    "value" : "",
    "group" : "Email notification details"
  }, {
    "idObject" : 22,
    "type" : "SEARCH_RESULT_NUMBER",
    "valueType" : "INTEGER",
    "commonName" : "Max number of results (this value indicates the max number of elements that will be returned from search - not the number of aggregated elements in the search box).",
    "isServerSide" : false,
    "value" : "100",
    "group" : "Point and click"
  }, {
    "idObject" : 1,
    "type" : "X_FRAME_DOMAIN",
    "valueType" : "URL",
    "commonName" : "Domain allowed to connect via x-frame technology",
    "isServerSide" : false,
    "value" : "https://minerva.uni.lu",
    "group" : "Server configuration"
  }, {
    "idObject" : 2,
    "type" : "CORS_DOMAIN",
    "valueType" : "BOOLEAN",
    "commonName" : "Disable CORS (when disabled 'ORIGIN' http header is required)",
    "isServerSide" : false,
    "value" : "false",
    "group" : "Server configuration"
  }, {
    "idObject" : 23,
    "type" : "BIG_FILE_STORAGE_DIR",
    "valueType" : "STRING",
    "commonName" : "Path to store big files",
    "isServerSide" : false,
    "value" : "minerva-big/",
    "group" : "Server configuration"
  }, {
    "idObject" : 24,
    "type" : "LEGEND_FILE_1",
    "valueType" : "URL",
    "commonName" : "Legend 1 image file",
    "isServerSide" : false,
    "value" : "resources/images/legend_a.png",
    "group" : "Legend and logo"
  }, {
    "idObject" : 25,
    "type" : "LEGEND_FILE_2",
    "valueType" : "URL",
    "commonName" : "Legend 2 image file",
    "isServerSide" : false,
    "value" : "resources/images/legend_b.png",
    "group" : "Legend and logo"
  }, {
    "idObject" : 26,
    "type" : "LEGEND_FILE_3",
    "valueType" : "URL",
    "commonName" : "Legend 3 image file",
    "isServerSide" : false,
    "value" : "resources/images/legend_c.png",
    "group" : "Legend and logo"
  }, {
    "idObject" : 27,
    "type" : "LEGEND_FILE_4",
    "valueType" : "URL",
    "commonName" : "Legend 4 image file",
    "isServerSide" : false,
    "value" : "resources/images/legend_d.png",
    "group" : "Legend and logo"
  }, {
    "idObject" : 28,
    "type" : "USER_MANUAL_FILE",
    "valueType" : "URL",
    "commonName" : "User manual file",
    "isServerSide" : false,
    "value" : "resources/other/user_guide.pdf",
    "group" : "Legend and logo"
  }, {
    "idObject" : 29,
    "type" : "MIN_COLOR_VAL",
    "valueType" : "COLOR",
    "commonName" : "Overlay color for negative values",
    "isServerSide" : false,
    "value" : "FF0000",
    "group" : "Overlays"
  }, {
    "idObject" : 30,
    "type" : "MAX_COLOR_VAL",
    "valueType" : "COLOR",
    "commonName" : "Overlay color for positive values",
    "isServerSide" : false,
    "value" : "0000FF",
    "group" : "Overlays"
  }, {
    "idObject" : 31,
    "type" : "SIMPLE_COLOR_VAL",
    "valueType" : "COLOR",
    "commonName" : "Overlay color when no values are defined",
    "isServerSide" : false,
    "value" : "00FF00",
    "group" : "Overlays"
  }, {
    "idObject" : 32,
    "type" : "NEUTRAL_COLOR_VAL",
    "valueType" : "COLOR",
    "commonName" : "Overlay color for value=0",
    "isServerSide" : false,
    "value" : "FFFFFF",
    "group" : "Overlays"
  }, {
    "idObject" : 33,
    "type" : "OVERLAY_OPACITY",
    "valueType" : "DOUBLE",
    "commonName" : "Opacity used when drawing data overlays (value between 0.0-1.0)",
    "isServerSide" : false,
    "value" : "0.8",
    "group" : "Overlays"
  }, {
    "idObject" : 34,
    "type" : "REQUEST_ACCOUNT_DEFAULT_CONTENT",
    "valueType" : "TEXT",
    "commonName" : "Email content used for requesting an account",
    "isServerSide" : false,
    "value" : "Dear Disease map team,\nI would like to request an account in the system.\nKind regards",
    "group" : "Email notification details"
  }, {
    "idObject" : 35,
    "type" : "SHOW_REACTION_TYPE",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction type",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 36,
    "type" : "TERMS_OF_USE",
    "valueType" : "URL",
    "commonName" : "URL of platform's Terms of Service",
    "isServerSide" : false,
    "value" : "",
    "group" : "Legend and logo"
  }, {
    "idObject" : 37,
    "type" : "COOKIE_POLICY_URL",
    "valueType" : "URL",
    "commonName" : "Privacy policy (url)",
    "isServerSide" : false,
    "value" : "default-cookie-policy.xhtml",
    "group" : "Server configuration"
  }, {
    "idObject" : 50,
    "type" : "SHOW_REACTION_TITLE",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction title",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 51,
    "type" : "SHOW_REACTION_NAME",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction name",
    "isServerSide" : false,
    "value" : "false",
    "group" : "Search panel options"
  }, {
    "idObject" : 52,
    "type" : "SHOW_REACTION_LINKED_SUBMAP",
    "valueType" : "BOOLEAN",
    "commonName" : "Show linked submap for reaction",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 53,
    "type" : "SHOW_REACTION_SYMBOL",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction symbol",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 54,
    "type" : "SHOW_REACTION_ABBREVIATION",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction abbreviation",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 55,
    "type" : "SHOW_REACTION_FORMULA",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction formula",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 56,
    "type" : "SHOW_REACTION_MECHANICAL_CONFIDENCE_SCORE",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction mechanical confidence score",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 57,
    "type" : "SHOW_REACTION_LOWER_BOUND",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction lower bound",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 58,
    "type" : "SHOW_REACTION_UPPER_BOUND",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction upper bound",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 59,
    "type" : "SHOW_REACTION_GENE_PROTEIN_REACTION",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction gene protein reaction",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 60,
    "type" : "SHOW_REACTION_SUBSYSTEM",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction subsystem",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 61,
    "type" : "SHOW_REACTION_SYNONYMS",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction synonyms",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 62,
    "type" : "SHOW_REACTION_DESCRIPTION",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction description",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 63,
    "type" : "SHOW_REACTION_ANNOTATIONS",
    "valueType" : "BOOLEAN",
    "commonName" : "Show reaction annotations",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 64,
    "type" : "SHOW_ELEMENT_TYPE",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element type",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 65,
    "type" : "SHOW_ELEMENT_TITLE",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element title",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 66,
    "type" : "SHOW_ELEMENT_LINKED_SUBMAP",
    "valueType" : "BOOLEAN",
    "commonName" : "Show linked submap for element",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 67,
    "type" : "SHOW_ELEMENT_GROUP_SIZE",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element group size",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 68,
    "type" : "SHOW_ELEMENT_COMPARTMENT",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element compartment",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 69,
    "type" : "SHOW_ELEMENT_FULL_NAME",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element full name",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 70,
    "type" : "SHOW_ELEMENT_SYMBOL",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element symbol",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 71,
    "type" : "SHOW_ELEMENT_ABBREVIATION",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element abbreviation",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 72,
    "type" : "SHOW_ELEMENT_FORMULA",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element formula",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 73,
    "type" : "SHOW_ELEMENT_FORMER_SYMBOLS",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element former symbol",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 74,
    "type" : "SHOW_ELEMENT_MODIFICATIONS",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element modifications",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 75,
    "type" : "SHOW_ELEMENT_CHARGE",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element charge",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 76,
    "type" : "SHOW_ELEMENT_SYNONYMS",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element synonyms",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 77,
    "type" : "SHOW_ELEMENT_DESCRIPTION",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element description",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 78,
    "type" : "SHOW_ELEMENT_ANNOTATIONS",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element annotations",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Search panel options"
  }, {
    "idObject" : 79,
    "type" : "SHOW_ELEMENT_ID",
    "valueType" : "BOOLEAN",
    "commonName" : "Show element id",
    "isServerSide" : false,
    "value" : "false",
    "group" : "Search panel options"
  }, {
    "idObject" : 3,
    "type" : "SESSION_LENGTH",
    "valueType" : "INTEGER",
    "commonName" : "Max session inactivity time (in seconds)",
    "isServerSide" : false,
    "value" : "7200",
    "group" : "Server configuration"
  }, {
    "idObject" : 80,
    "type" : "MAX_NUMBER_OF_MAP_LEVELS",
    "valueType" : "INTEGER",
    "commonName" : "Max number of map zoom levels",
    "isServerSide" : false,
    "value" : "10",
    "group" : "Point and click"
  }, {
    "idObject" : 81,
    "type" : "DAPI_LOGIN",
    "valueType" : "STRING",
    "commonName" : "Login to Data-API system",
    "isServerSide" : false,
    "value" : "",
    "group" : "Data-API configuration"
  }, {
    "idObject" : 82,
    "type" : "DAPI_PASSWORD",
    "valueType" : "PASSWORD",
    "commonName" : "Password to Data-API system",
    "isServerSide" : false,
    "group" : "Data-API configuration"
  }, {
    "idObject" : 83,
    "type" : "MINERVA_ROOT",
    "valueType" : "URL",
    "commonName" : "Minerva root url",
    "isServerSide" : false,
    "value" : "https://minerva-dev.lcsb.uni.lu/minerva/",
    "group" : "Server configuration"
  }, {
    "idObject" : 84,
    "type" : "REQUEST_ACCOUNT_DEFAULT_TITLE",
    "valueType" : "STRING",
    "commonName" : "Email title used for requesting an account",
    "isServerSide" : false,
    "value" : "MINERVA account request",
    "group" : "Email notification details"
  }, {
    "idObject" : 85,
    "type" : "CUSTOM_CSS",
    "valueType" : "TEXT",
    "commonName" : "Custom CSS",
    "isServerSide" : false,
    "value" : "",
    "group" : "Legend and logo"
  }, {
    "idObject" : 86,
    "type" : "ORCID_CLIENT_ID",
    "valueType" : "TEXT",
    "commonName" : "Orcid Client ID",
    "isServerSide" : false,
    "value" : "",
    "group" : "OAuth conifguration"
  }, {
    "idObject" : 87,
    "type" : "ORCID_CLIENT_SECRET",
    "valueType" : "PASSWORD",
    "commonName" : "Orcid Client Secret",
    "isServerSide" : false,
    "group" : "OAuth conifguration"
  }, {
    "idObject" : 88,
    "type" : "ALLOW_AUTO_REGISTER",
    "valueType" : "BOOLEAN",
    "commonName" : "Allow users to create accounts",
    "isServerSide" : false,
    "value" : "false",
    "group" : "Server configuration"
  }, {
    "idObject" : 89,
    "type" : "REQUIRE_APPROVAL_FOR_AUTO_REGISTERED_USERS",
    "valueType" : "BOOLEAN",
    "commonName" : "Require admin approval for auto-registered accounts",
    "isServerSide" : false,
    "value" : "true",
    "group" : "Server configuration"
  }, {
    "idObject" : 90,
    "type" : "ENFORCE_OLD_INTERFACE",
    "valueType" : "BOOLEAN",
    "commonName" : "Enforce old interface by default",
    "isServerSide" : false,
    "value" : "false",
    "group" : "Server configuration"
  } ],
  "imageFormats" : [ {
    "name" : "PNG image",
    "handler" : "lcsb.mapviewer.converter.graphics.PngImageGenerator",
    "extension" : "png"
  }, {
    "name" : "PDF image",
    "handler" : "lcsb.mapviewer.converter.graphics.PdfImageGenerator",
    "extension" : "pdf"
  }, {
    "name" : "SVG image",
    "handler" : "lcsb.mapviewer.converter.graphics.SvgImageGenerator",
    "extension" : "svg"
  } ],
  "modelFormats" : [ {
    "name" : "CellDesigner SBML",
    "handler" : "lcsb.mapviewer.converter.model.celldesigner.CellDesignerXmlParser",
    "extension" : "xml",
    "extensions" : [ "xml" ]
  }, {
    "name" : "SBGN-ML",
    "handler" : "lcsb.mapviewer.converter.model.sbgnml.SbgnmlXmlConverter",
    "extension" : "sbgn",
    "extensions" : [ "sbgn" ]
  }, {
    "name" : "SBML",
    "handler" : "lcsb.mapviewer.converter.model.sbml.SbmlParser",
    "extension" : "xml",
    "extensions" : [ "xml", "sbml" ]
  }, {
    "name" : "GPML",
    "handler" : "lcsb.mapviewer.wikipathway.GpmlParser",
    "extension" : "gpml",
    "extensions" : [ "gpml" ]
  } ],
  "overlayTypes" : [ {
    "name" : "GENERIC"
  }, {
    "name" : "GENETIC_VARIANT"
  } ],
  "elementTypes" : [ {
    "className" : "lcsb.mapviewer.model.map.species.Element",
    "name" : "Element",
    "parentClass" : "lcsb.mapviewer.model.map.BioEntity"
  }, {
    "className" : "lcsb.mapviewer.model.map.compartment.Compartment",
    "name" : "Compartment",
    "parentClass" : "lcsb.mapviewer.model.map.species.Element"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Species",
    "name" : "Species",
    "parentClass" : "lcsb.mapviewer.model.map.species.Element"
  }, {
    "className" : "lcsb.mapviewer.model.map.compartment.LeftSquareCompartment",
    "name" : "Compartment",
    "parentClass" : "lcsb.mapviewer.model.map.compartment.Compartment"
  }, {
    "className" : "lcsb.mapviewer.model.map.compartment.BottomSquareCompartment",
    "name" : "Compartment",
    "parentClass" : "lcsb.mapviewer.model.map.compartment.Compartment"
  }, {
    "className" : "lcsb.mapviewer.model.map.compartment.RightSquareCompartment",
    "name" : "Compartment",
    "parentClass" : "lcsb.mapviewer.model.map.compartment.Compartment"
  }, {
    "className" : "lcsb.mapviewer.model.map.compartment.TopSquareCompartment",
    "name" : "Compartment",
    "parentClass" : "lcsb.mapviewer.model.map.compartment.Compartment"
  }, {
    "className" : "lcsb.mapviewer.model.map.compartment.SquareCompartment",
    "name" : "Compartment",
    "parentClass" : "lcsb.mapviewer.model.map.compartment.Compartment"
  }, {
    "className" : "lcsb.mapviewer.model.map.compartment.OvalCompartment",
    "name" : "Compartment",
    "parentClass" : "lcsb.mapviewer.model.map.compartment.Compartment"
  }, {
    "className" : "lcsb.mapviewer.model.map.compartment.PathwayCompartment",
    "name" : "Pathway",
    "parentClass" : "lcsb.mapviewer.model.map.compartment.Compartment"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.AntisenseRna",
    "name" : "Antisense RNA",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Chemical",
    "name" : "Chemical",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Complex",
    "name" : "Complex",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Degraded",
    "name" : "Degraded",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Drug",
    "name" : "Drug",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Gene",
    "name" : "Gene",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Phenotype",
    "name" : "Phenotype",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Protein",
    "name" : "Protein",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Rna",
    "name" : "RNA",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Unknown",
    "name" : "Unknown",
    "parentClass" : "lcsb.mapviewer.model.map.species.Species"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.Ion",
    "name" : "Ion",
    "parentClass" : "lcsb.mapviewer.model.map.species.Chemical"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.SimpleMolecule",
    "name" : "Simple molecule",
    "parentClass" : "lcsb.mapviewer.model.map.species.Chemical"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.TruncatedProtein",
    "name" : "Protein",
    "parentClass" : "lcsb.mapviewer.model.map.species.Protein"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.GenericProtein",
    "name" : "Protein",
    "parentClass" : "lcsb.mapviewer.model.map.species.Protein"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.IonChannelProtein",
    "name" : "Protein",
    "parentClass" : "lcsb.mapviewer.model.map.species.Protein"
  }, {
    "className" : "lcsb.mapviewer.model.map.species.ReceptorProtein",
    "name" : "Protein",
    "parentClass" : "lcsb.mapviewer.model.map.species.Protein"
  } ],
  "reactionTypes" : [ {
    "className" : "lcsb.mapviewer.model.map.reaction.Reaction",
    "name" : "Generic Reaction",
    "parentClass" : "lcsb.mapviewer.model.map.BioEntity"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.CatalysisReaction",
    "name" : "Catalysis",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.DissociationReaction",
    "name" : "Dissociation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.HeterodimerAssociationReaction",
    "name" : "Heterodimer association",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.InhibitionReaction",
    "name" : "Inhibition",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.KnownTransitionOmittedReaction",
    "name" : "Known transition omitted",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.ModulationReaction",
    "name" : "Modulation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.NegativeInfluenceReaction",
    "name" : "Negative influence",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.PhysicalStimulationReaction",
    "name" : "Physical stimulation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.PositiveInfluenceReaction",
    "name" : "Positive influence",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.ReducedModulationReaction",
    "name" : "Reduced modulation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.ReducedPhysicalStimulationReaction",
    "name" : "Reduced physical stimulation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.ReducedTriggerReaction",
    "name" : "Reduced trigger",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.StateTransitionReaction",
    "name" : "State transition",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.TranscriptionReaction",
    "name" : "Transcription",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.TranslationReaction",
    "name" : "Translation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.TransportReaction",
    "name" : "Transport",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.TriggerReaction",
    "name" : "Trigger",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.TruncationReaction",
    "name" : "Truncation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.UnknownCatalysisReaction",
    "name" : "Unknown catalysis",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.UnknownInhibitionReaction",
    "name" : "Unknown inhibition",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.UnknownNegativeInfluenceReaction",
    "name" : "Unknown negative influence",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.UnknownPositiveInfluenceReaction",
    "name" : "Unknown positive influence",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.UnknownReducedModulationReaction",
    "name" : "Unknown reduced modulation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.UnknownReducedPhysicalStimulationReaction",
    "name" : "Unknown reduced physical stimulation",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.UnknownReducedTriggerReaction",
    "name" : "Unknown reduced trigger",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  }, {
    "className" : "lcsb.mapviewer.model.map.reaction.type.UnknownTransitionReaction",
    "name" : "Unknown transition",
    "parentClass" : "lcsb.mapviewer.model.map.reaction.Reaction"
  } ],
  "miriamTypes" : {
    "ABS" : {
      "commonName" : "ABS",
      "homepage" : "http://genome.crg.es/datasets/abs2005/",
      "registryIdentifier" : "MIR:00000277",
      "uris" : [ "urn:miriam:abs", "http://identifiers.org/abs/", "http://identifiers.org/abs", "https://identifiers.org/abs/", "https://identifiers.org/abs" ]
    },
    "ACEVIEW_WORM" : {
      "commonName" : "Aceview Worm",
      "homepage" : "https://www.ncbi.nlm.nih.gov/IEB/Research/Acembly/index.html?worm",
      "registryIdentifier" : "MIR:00000282",
      "uris" : [ "urn:miriam:aceview.worm", "http://identifiers.org/aceview.worm/", "http://identifiers.org/aceview.worm", "https://identifiers.org/aceview.worm/", "https://identifiers.org/aceview.worm" ]
    },
    "AFFYMETRIX_PROBESET" : {
      "commonName" : "Affymetrix Probeset",
      "homepage" : "http://www.affymetrix.com/",
      "registryIdentifier" : "MIR:00000394",
      "uris" : [ "urn:miriam:affy.probeset", "http://identifiers.org/affy.probeset/", "http://identifiers.org/affy.probeset", "https://identifiers.org/affy.probeset/", "https://identifiers.org/affy.probeset" ]
    },
    "AFTOL" : {
      "commonName" : "AFTOL",
      "homepage" : "http://aftol.org/data.php",
      "registryIdentifier" : "MIR:00000411",
      "uris" : [ "urn:miriam:aftol.taxonomy", "http://identifiers.org/aftol.taxonomy/", "http://identifiers.org/aftol.taxonomy", "https://identifiers.org/aftol.taxonomy/", "https://identifiers.org/aftol.taxonomy" ]
    },
    "ALLERGOME" : {
      "commonName" : "Allergome",
      "homepage" : "http://www.allergome.org/",
      "registryIdentifier" : "MIR:00000334",
      "uris" : [ "urn:miriam:allergome", "http://identifiers.org/allergome/", "http://identifiers.org/allergome", "https://identifiers.org/allergome/", "https://identifiers.org/allergome" ]
    },
    "AMOEBADB" : {
      "commonName" : "AmoebaDB",
      "homepage" : "http://amoebadb.org/amoeba/",
      "registryIdentifier" : "MIR:00000148",
      "uris" : [ "urn:miriam:amoebadb", "http://identifiers.org/amoebadb/", "http://identifiers.org/amoebadb", "https://identifiers.org/amoebadb/", "https://identifiers.org/amoebadb" ]
    },
    "ANATOMICAL_THERAPEUTIC_CHEMICAL" : {
      "commonName" : "Anatomical Therapeutic Chemical",
      "homepage" : "http://www.whocc.no/atc_ddd_index/",
      "registryIdentifier" : "MIR:00000088",
      "uris" : [ "urn:miriam:atc", "http://identifiers.org/atc/", "http://identifiers.org/atc", "https://identifiers.org/atc/", "https://identifiers.org/atc" ]
    },
    "ANATOMICAL_THERAPEUTIC_CHEMICAL_VETINARY" : {
      "commonName" : "Anatomical Therapeutic Chemical Vetinary",
      "homepage" : "http://www.whocc.no/atcvet/atcvet_index/",
      "registryIdentifier" : "MIR:00000267",
      "uris" : [ "urn:miriam:atcvet", "http://identifiers.org/atcvet/", "http://identifiers.org/atcvet", "https://identifiers.org/atcvet/", "https://identifiers.org/atcvet" ]
    },
    "ANIMAL_DIVERSITY_WEB" : {
      "commonName" : "Animal Diversity Web",
      "homepage" : "https://animaldiversity.org/",
      "registryIdentifier" : "MIR:00000492",
      "uris" : [ "urn:miriam:adw", "http://identifiers.org/adw/", "http://identifiers.org/adw", "https://identifiers.org/adw/", "https://identifiers.org/adw" ]
    },
    "ANIMAL_GENOME_CATTLE_QTL" : {
      "commonName" : "Animal Genome Cattle QTL",
      "homepage" : "https://www.animalgenome.org/QTLdb",
      "registryIdentifier" : "MIR:00000504",
      "uris" : [ "urn:miriam:cattleqtldb", "http://identifiers.org/cattleqtldb/", "http://identifiers.org/cattleqtldb", "https://identifiers.org/cattleqtldb/", "https://identifiers.org/cattleqtldb" ]
    },
    "ANIMAL_GENOME_CHICKEN_QTL" : {
      "commonName" : "Animal Genome Chicken QTL",
      "homepage" : "https://www.animalgenome.org/QTLdb",
      "registryIdentifier" : "MIR:00000505",
      "uris" : [ "urn:miriam:chickenqtldb", "http://identifiers.org/chickenqtldb/", "http://identifiers.org/chickenqtldb", "https://identifiers.org/chickenqtldb/", "https://identifiers.org/chickenqtldb" ]
    },
    "ANIMAL_GENOME_PIG_QTL" : {
      "commonName" : "Animal Genome Pig QTL",
      "homepage" : "https://www.animalgenome.org/QTLdb",
      "registryIdentifier" : "MIR:00000506",
      "uris" : [ "urn:miriam:pigqtldb", "http://identifiers.org/pigqtldb/", "http://identifiers.org/pigqtldb", "https://identifiers.org/pigqtldb/", "https://identifiers.org/pigqtldb" ]
    },
    "ANIMAL_GENOME_SHEEP_QTL" : {
      "commonName" : "Animal Genome Sheep QTL",
      "homepage" : "https://www.animalgenome.org/QTLdb",
      "registryIdentifier" : "MIR:00000507",
      "uris" : [ "urn:miriam:sheepqtldb", "http://identifiers.org/sheepqtldb/", "http://identifiers.org/sheepqtldb", "https://identifiers.org/sheepqtldb/", "https://identifiers.org/sheepqtldb" ]
    },
    "ANIMAL_TFDB_FAMILY" : {
      "commonName" : "Animal TFDB Family",
      "homepage" : "http://www.bioguo.org/AnimalTFDB/family_index.php",
      "registryIdentifier" : "MIR:00000316",
      "uris" : [ "urn:miriam:atfdb.family", "http://identifiers.org/atfdb.family/", "http://identifiers.org/atfdb.family", "https://identifiers.org/atfdb.family/", "https://identifiers.org/atfdb.family" ]
    },
    "ANTIBIOTIC_RESISTANCE_GENES_DATABASE" : {
      "commonName" : "Antibiotic Resistance Genes Database",
      "homepage" : "http://ardb.cbcb.umd.edu/",
      "registryIdentifier" : "MIR:00000522",
      "uris" : [ "urn:miriam:ardb", "http://identifiers.org/ardb/", "http://identifiers.org/ardb", "https://identifiers.org/ardb/", "https://identifiers.org/ardb" ]
    },
    "ANTIBODY_REGISTRY" : {
      "commonName" : "Antibody Registry",
      "homepage" : "http://antibodyregistry.org/",
      "registryIdentifier" : "MIR:00000516",
      "uris" : [ "urn:miriam:antibodyregistry", "http://identifiers.org/antibodyregistry/", "http://identifiers.org/antibodyregistry", "https://identifiers.org/antibodyregistry/", "https://identifiers.org/antibodyregistry" ]
    },
    "ANTWEB" : {
      "commonName" : "AntWeb",
      "homepage" : "http://www.antweb.org/",
      "registryIdentifier" : "MIR:00000146",
      "uris" : [ "urn:miriam:antweb", "http://identifiers.org/antweb/", "http://identifiers.org/antweb", "https://identifiers.org/antweb/", "https://identifiers.org/antweb" ]
    },
    "APD" : {
      "commonName" : "APD",
      "homepage" : "http://aps.unmc.edu/AP/",
      "registryIdentifier" : "MIR:00000278",
      "uris" : [ "urn:miriam:apd", "http://identifiers.org/apd/", "http://identifiers.org/apd", "https://identifiers.org/apd/", "https://identifiers.org/apd" ]
    },
    "APHIDBASE_TRANSCRIPT" : {
      "commonName" : "AphidBase Transcript",
      "homepage" : "http://www.aphidbase.com/aphidbase",
      "registryIdentifier" : "MIR:00000393",
      "uris" : [ "urn:miriam:aphidbase.transcript", "http://identifiers.org/aphidbase.transcript/", "http://identifiers.org/aphidbase.transcript", "https://identifiers.org/aphidbase.transcript/", "https://identifiers.org/aphidbase.transcript" ]
    },
    "ARACHNOSERVER" : {
      "commonName" : "ArachnoServer",
      "homepage" : "http://www.arachnoserver.org/",
      "registryIdentifier" : "MIR:00000193",
      "uris" : [ "urn:miriam:arachnoserver", "http://identifiers.org/arachnoserver/", "http://identifiers.org/arachnoserver", "https://identifiers.org/arachnoserver/", "https://identifiers.org/arachnoserver" ]
    },
    "ARRAYEXPRESS" : {
      "commonName" : "ArrayExpress",
      "homepage" : "https://www.ebi.ac.uk/arrayexpress/",
      "registryIdentifier" : "MIR:00000036",
      "uris" : [ "urn:miriam:arrayexpress", "http://identifiers.org/arrayexpress/", "http://identifiers.org/arrayexpress", "https://identifiers.org/arrayexpress/", "https://identifiers.org/arrayexpress" ]
    },
    "ARRAYEXPRESS_PLATFORM" : {
      "commonName" : "ArrayExpress Platform",
      "homepage" : "https://www.ebi.ac.uk/arrayexpress/",
      "registryIdentifier" : "MIR:00000294",
      "uris" : [ "urn:miriam:arrayexpress.platform", "http://identifiers.org/arrayexpress.platform/", "http://identifiers.org/arrayexpress.platform", "https://identifiers.org/arrayexpress.platform/", "https://identifiers.org/arrayexpress.platform" ]
    },
    "ARXIV" : {
      "commonName" : "arXiv",
      "homepage" : "https://arxiv.org/",
      "registryIdentifier" : "MIR:00000035",
      "uris" : [ "urn:miriam:arxiv", "urn:oai:arXiv.org", "http://identifiers.org/arxiv/", "http://identifiers.org/arxiv", "https://identifiers.org/arxiv/", "https://identifiers.org/arxiv" ]
    },
    "ASAP" : {
      "commonName" : "ASAP",
      "homepage" : "http://asap.ahabs.wisc.edu/asap/home.php",
      "registryIdentifier" : "MIR:00000283",
      "uris" : [ "urn:miriam:asap", "http://identifiers.org/asap/", "http://identifiers.org/asap", "https://identifiers.org/asap/", "https://identifiers.org/asap" ]
    },
    "ASPGD_LOCUS" : {
      "commonName" : "AspGD Locus",
      "homepage" : "http://www.aspgd.org/",
      "registryIdentifier" : "MIR:00000412",
      "uris" : [ "urn:miriam:aspgd.locus", "http://identifiers.org/aspgd.locus/", "http://identifiers.org/aspgd.locus", "https://identifiers.org/aspgd.locus/", "https://identifiers.org/aspgd.locus" ]
    },
    "ASPGD_PROTEIN" : {
      "commonName" : "AspGD Protein",
      "homepage" : "http://www.aspgd.org/",
      "registryIdentifier" : "MIR:00000413",
      "uris" : [ "urn:miriam:aspgd.protein", "http://identifiers.org/aspgd.protein/", "http://identifiers.org/aspgd.protein", "https://identifiers.org/aspgd.protein/", "https://identifiers.org/aspgd.protein" ]
    },
    "ATCC" : {
      "commonName" : "ATCC",
      "homepage" : "http://www.atcc.org/",
      "registryIdentifier" : "MIR:00000284",
      "uris" : [ "urn:miriam:atcc", "http://identifiers.org/atcc/", "http://identifiers.org/atcc", "https://identifiers.org/atcc/", "https://identifiers.org/atcc" ]
    },
    "AUTDB" : {
      "commonName" : "AutDB",
      "homepage" : "http://autism.mindspec.org/autdb/",
      "registryIdentifier" : "MIR:00000415",
      "uris" : [ "urn:miriam:autdb", "http://identifiers.org/autdb/", "http://identifiers.org/autdb", "https://identifiers.org/autdb/", "https://identifiers.org/autdb" ]
    },
    "BACMAP_BIOGRAPHY" : {
      "commonName" : "BacMap Biography",
      "homepage" : "http://bacmap.wishartlab.com/",
      "registryIdentifier" : "MIR:00000361",
      "uris" : [ "urn:miriam:bacmap.biog", "http://identifiers.org/bacmap.biog/", "http://identifiers.org/bacmap.biog", "https://identifiers.org/bacmap.biog/", "https://identifiers.org/bacmap.biog" ]
    },
    "BACMAP_MAP" : {
      "commonName" : "BacMap Map",
      "homepage" : "http://bacmap.wishartlab.com/",
      "registryIdentifier" : "MIR:00000416",
      "uris" : [ "urn:miriam:bacmap.map", "http://identifiers.org/bacmap.map/", "http://identifiers.org/bacmap.map", "https://identifiers.org/bacmap.map/", "https://identifiers.org/bacmap.map" ]
    },
    "BDGP_EST" : {
      "commonName" : "BDGP EST",
      "homepage" : "https://www.ncbi.nlm.nih.gov/dbEST/index.html",
      "registryIdentifier" : "MIR:00000285",
      "uris" : [ "urn:miriam:bdgp.est", "http://identifiers.org/bdgp.est/", "http://identifiers.org/bdgp.est", "https://identifiers.org/bdgp.est/", "https://identifiers.org/bdgp.est" ]
    },
    "BDGP_INSERTION_DB" : {
      "commonName" : "BDGP insertion DB",
      "homepage" : "http://flypush.imgen.bcm.tmc.edu/pscreen/",
      "registryIdentifier" : "MIR:00000156",
      "uris" : [ "urn:miriam:bdgp.insertion", "http://identifiers.org/bdgp.insertion/", "http://identifiers.org/bdgp.insertion", "https://identifiers.org/bdgp.insertion/", "https://identifiers.org/bdgp.insertion" ]
    },
    "BEETLEBASE" : {
      "commonName" : "BeetleBase",
      "homepage" : "http://beetlebase.org/",
      "registryIdentifier" : "MIR:00000157",
      "uris" : [ "urn:miriam:beetlebase", "http://identifiers.org/beetlebase/", "http://identifiers.org/beetlebase", "https://identifiers.org/beetlebase/", "https://identifiers.org/beetlebase" ]
    },
    "BGEE_FAMILY" : {
      "commonName" : "Bgee family",
      "homepage" : "http://bgee.unil.ch/bgee/bgee",
      "registryIdentifier" : "MIR:00000417",
      "uris" : [ "urn:miriam:bgee.family", "http://identifiers.org/bgee.family/", "http://identifiers.org/bgee.family", "https://identifiers.org/bgee.family/", "https://identifiers.org/bgee.family" ]
    },
    "BGEE_GENE" : {
      "commonName" : "Bgee gene",
      "homepage" : "https://bgee.org/",
      "registryIdentifier" : "MIR:00000418",
      "uris" : [ "urn:miriam:bgee.gene", "http://identifiers.org/bgee.gene/", "http://identifiers.org/bgee.gene", "https://identifiers.org/bgee.gene/", "https://identifiers.org/bgee.gene" ]
    },
    "BGEE_ORGAN" : {
      "commonName" : "Bgee organ",
      "homepage" : "http://bgee.unil.ch/bgee/bgee",
      "registryIdentifier" : "MIR:00000420",
      "uris" : [ "urn:miriam:bgee.organ", "http://identifiers.org/bgee.organ/", "http://identifiers.org/bgee.organ", "https://identifiers.org/bgee.organ/", "https://identifiers.org/bgee.organ" ]
    },
    "BGEE_STAGE" : {
      "commonName" : "Bgee stage",
      "homepage" : "http://bgee.unil.ch/bgee/bgee",
      "registryIdentifier" : "MIR:00000419",
      "uris" : [ "urn:miriam:bgee.stage", "http://identifiers.org/bgee.stage/", "http://identifiers.org/bgee.stage", "https://identifiers.org/bgee.stage/", "https://identifiers.org/bgee.stage" ]
    },
    "BINDINGDB" : {
      "commonName" : "BindingDB",
      "homepage" : "https://www.bindingdb.org",
      "registryIdentifier" : "MIR:00000264",
      "uris" : [ "urn:miriam:bindingDB", "http://identifiers.org/bindingdb/", "http://identifiers.org/bindingdb", "https://identifiers.org/bindingdb/", "https://identifiers.org/bindingdb" ]
    },
    "BIOCARTA_PATHWAY" : {
      "commonName" : "BioCarta Pathway",
      "homepage" : "https://www.biocarta.com/",
      "registryIdentifier" : "MIR:00000421",
      "uris" : [ "urn:miriam:biocarta.pathway", "http://identifiers.org/biocarta.pathway/", "http://identifiers.org/biocarta.pathway", "https://identifiers.org/biocarta.pathway/", "https://identifiers.org/biocarta.pathway" ]
    },
    "BIOCATALOGUE" : {
      "commonName" : "BioCatalogue",
      "homepage" : "https://www.biocatalogue.org/",
      "registryIdentifier" : "MIR:00000140",
      "uris" : [ "urn:miriam:biocatalogue.service", "http://identifiers.org/biocatalogue.service/", "http://identifiers.org/biocatalogue.service", "https://identifiers.org/biocatalogue.service/", "https://identifiers.org/biocatalogue.service" ]
    },
    "BIOCYC" : {
      "commonName" : "BioCyc",
      "homepage" : "http://biocyc.org",
      "registryIdentifier" : "MIR:00000194",
      "uris" : [ "urn:miriam:biocyc", "http://identifiers.org/biocyc/", "http://identifiers.org/biocyc", "https://identifiers.org/biocyc/", "https://identifiers.org/biocyc" ]
    },
    "BIOGRID" : {
      "commonName" : "BioGRID",
      "homepage" : "http://thebiogrid.org/",
      "registryIdentifier" : "MIR:00000058",
      "uris" : [ "urn:miriam:biogrid", "http://identifiers.org/biogrid/", "http://identifiers.org/biogrid", "https://identifiers.org/biogrid/", "https://identifiers.org/biogrid" ]
    },
    "BIOKC" : {
      "commonName" : "BioKC",
      "homepage" : "https://biokb.lcsb.uni.lu/",
      "registryIdentifier" : "MIR:00000995",
      "uris" : [ "http://identifiers.org/biokc", "http://identifiers.org/biokc/", "https://identifiers.org/biokc", "https://identifiers.org/biokc/" ]
    },
    "BIOMODELS_DATABASE" : {
      "commonName" : "BioModels Database",
      "homepage" : "https://www.ebi.ac.uk/biomodels/",
      "registryIdentifier" : "MIR:00000007",
      "uris" : [ "urn:miriam:biomodels.db", "http://identifiers.org/biomodels.db/", "http://identifiers.org/biomodels.db", "https://identifiers.org/biomodels.db/", "https://identifiers.org/biomodels.db" ]
    },
    "BIONUMBERS" : {
      "commonName" : "BioNumbers",
      "homepage" : "https://bionumbers.hms.harvard.edu",
      "registryIdentifier" : "MIR:00000101",
      "uris" : [ "urn:miriam:bionumbers", "http://identifiers.org/bionumbers/", "http://identifiers.org/bionumbers", "https://identifiers.org/bionumbers/", "https://identifiers.org/bionumbers" ]
    },
    "BIOPORTAL" : {
      "commonName" : "BioPortal",
      "homepage" : "http://bioportal.bioontology.org/",
      "registryIdentifier" : "MIR:00000187",
      "uris" : [ "urn:miriam:bioportal", "http://identifiers.org/bioportal/", "http://identifiers.org/bioportal", "https://identifiers.org/bioportal/", "https://identifiers.org/bioportal" ]
    },
    "BIOPROJECT" : {
      "commonName" : "BioProject",
      "homepage" : "http://trace.ddbj.nig.ac.jp/bioproject/",
      "registryIdentifier" : "MIR:00000349",
      "uris" : [ "urn:miriam:bioproject", "http://identifiers.org/bioproject/", "http://identifiers.org/bioproject", "https://identifiers.org/bioproject/", "https://identifiers.org/bioproject" ]
    },
    "BIOSAMPLE" : {
      "commonName" : "BioSample",
      "homepage" : "https://www.ebi.ac.uk/biosamples/",
      "registryIdentifier" : "MIR:00000350",
      "uris" : [ "urn:miriam:biosample", "http://identifiers.org/biosample/", "http://identifiers.org/biosample", "https://identifiers.org/biosample/", "https://identifiers.org/biosample" ]
    },
    "BIOSYSTEMS" : {
      "commonName" : "BioSystems",
      "homepage" : "https://www.ncbi.nlm.nih.gov/biosystems/",
      "registryIdentifier" : "MIR:00000097",
      "uris" : [ "urn:miriam:biosystems", "http://identifiers.org/biosystems/", "http://identifiers.org/biosystems", "https://identifiers.org/biosystems/", "https://identifiers.org/biosystems" ]
    },
    "BITTERDB_COMPOUND" : {
      "commonName" : "BitterDB Compound",
      "homepage" : "http://bitterdb.agri.huji.ac.il/dbbitter.php",
      "registryIdentifier" : "MIR:00000348",
      "uris" : [ "urn:miriam:bitterdb.cpd", "http://identifiers.org/bitterdb.cpd/", "http://identifiers.org/bitterdb.cpd", "https://identifiers.org/bitterdb.cpd/", "https://identifiers.org/bitterdb.cpd" ]
    },
    "BITTERDB_RECEPTOR" : {
      "commonName" : "BitterDB Receptor",
      "homepage" : "http://bitterdb.agri.huji.ac.il/dbbitter.php",
      "registryIdentifier" : "MIR:00000347",
      "uris" : [ "urn:miriam:bitterdb.rec", "http://identifiers.org/bitterdb.rec/", "http://identifiers.org/bitterdb.rec", "https://identifiers.org/bitterdb.rec/", "https://identifiers.org/bitterdb.rec" ]
    },
    "BOLD_TAXONOMY" : {
      "commonName" : "BOLD Taxonomy",
      "homepage" : "http://www.boldsystems.org/",
      "registryIdentifier" : "MIR:00000158",
      "uris" : [ "urn:miriam:bold.taxonomy", "http://identifiers.org/bold.taxonomy/", "http://identifiers.org/bold.taxonomy", "https://identifiers.org/bold.taxonomy/", "https://identifiers.org/bold.taxonomy" ]
    },
    "BRENDA" : {
      "commonName" : "BRENDA",
      "homepage" : "http://www.brenda-enzymes.org",
      "registryIdentifier" : "MIR:00000071",
      "uris" : [ "urn:miriam:brenda", "http://identifiers.org/brenda/", "http://identifiers.org/brenda", "https://identifiers.org/brenda/", "https://identifiers.org/brenda" ]
    },
    "BRENDA_TISSUE_ONTOLOGY" : {
      "commonName" : "Brenda Tissue Ontology",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/bto",
      "registryIdentifier" : "MIR:00000111",
      "uris" : [ "urn:miriam:bto", "urn:miriam:obo.bto", "http://identifiers.org/bto/", "http://identifiers.org/obo.bto/", "http://identifiers.org/BTO", "https://identifiers.org/bto/", "https://identifiers.org/obo.bto/", "https://identifiers.org/BTO" ]
    },
    "BROAD_FUNGAL_GENOME_INITIATIVE" : {
      "commonName" : "Broad Fungal Genome Initiative",
      "homepage" : "https://www.broadinstitute.org/annotation/genome/magnaporthe_grisea/",
      "registryIdentifier" : "MIR:00000438",
      "uris" : [ "urn:miriam:broad", "http://identifiers.org/broad/", "http://identifiers.org/broad", "https://identifiers.org/broad/", "https://identifiers.org/broad" ]
    },
    "BUGBASE_EXPT" : {
      "commonName" : "BugBase Expt",
      "homepage" : "http://bugs.sgul.ac.uk/E-BUGS",
      "registryIdentifier" : "MIR:00000404",
      "uris" : [ "urn:miriam:bugbase.expt", "http://identifiers.org/bugbase.expt/", "http://identifiers.org/bugbase.expt", "https://identifiers.org/bugbase.expt/", "https://identifiers.org/bugbase.expt" ]
    },
    "BUGBASE_PROTOCOL" : {
      "commonName" : "BugBase Protocol",
      "homepage" : "http://bugs.sgul.ac.uk/E-BUGS",
      "registryIdentifier" : "MIR:00000403",
      "uris" : [ "urn:miriam:bugbase.protocol", "http://identifiers.org/bugbase.protocol/", "http://identifiers.org/bugbase.protocol", "https://identifiers.org/bugbase.protocol/", "https://identifiers.org/bugbase.protocol" ]
    },
    "BYKDB" : {
      "commonName" : "BYKdb",
      "homepage" : "https://bykdb.ibcp.fr/BYKdb/",
      "registryIdentifier" : "MIR:00000253",
      "uris" : [ "urn:miriam:bykdb", "http://identifiers.org/bykdb/", "http://identifiers.org/bykdb", "https://identifiers.org/bykdb/", "https://identifiers.org/bykdb" ]
    },
    "BiGG_COMPARTMENT" : {
      "commonName" : "BiGG Compartment",
      "homepage" : "http://bigg.ucsd.edu/compartments/",
      "registryIdentifier" : "MIR:00000555",
      "uris" : [ "urn:miriam:bigg.compartment", "http://identifiers.org/bigg.compartment/", "http://identifiers.org/bigg.compartment", "https://identifiers.org/bigg.compartment/", "https://identifiers.org/bigg.compartment" ]
    },
    "BiGG_METABOLITE" : {
      "commonName" : "BiGG Metabolite",
      "homepage" : "http://bigg.ucsd.edu/universal/metabolites",
      "registryIdentifier" : "MIR:00000556",
      "uris" : [ "urn:miriam:bigg.metabolite", "http://identifiers.org/bigg.metabolite/", "http://identifiers.org/bigg.metabolite", "https://identifiers.org/bigg.metabolite/", "https://identifiers.org/bigg.metabolite" ]
    },
    "BiGG_REACTIONS" : {
      "commonName" : "BiGG Reaction",
      "homepage" : "http://bigg.ucsd.edu/universal/reactions",
      "registryIdentifier" : "MIR:00000557",
      "uris" : [ "urn:miriam:bigg.reaction", "http://identifiers.org/bigg.reaction/", "http://identifiers.org/bigg.reaction", "https://identifiers.org/bigg.reaction/", "https://identifiers.org/bigg.reaction" ]
    },
    "CANADIAN_DRUG_PRODUCT_DATABASE" : {
      "commonName" : "Canadian Drug Product Database",
      "homepage" : "http://webprod3.hc-sc.gc.ca/dpd-bdpp/index-eng.jsp",
      "registryIdentifier" : "MIR:00000272",
      "uris" : [ "urn:miriam:cdpd", "http://identifiers.org/cdpd/", "http://identifiers.org/cdpd", "https://identifiers.org/cdpd/", "https://identifiers.org/cdpd" ]
    },
    "CANDIDA_GENOME_DATABASE" : {
      "commonName" : "Candida Genome Database",
      "homepage" : "http://www.candidagenome.org/",
      "registryIdentifier" : "MIR:00000145",
      "uris" : [ "urn:miriam:cgd", "http://identifiers.org/cgd/", "http://identifiers.org/cgd", "https://identifiers.org/cgd/", "https://identifiers.org/cgd" ]
    },
    "CAPS_DB" : {
      "commonName" : "CAPS-DB",
      "homepage" : "http://www.bioinsilico.org/cgi-bin/CAPSDB/staticHTML/home",
      "registryIdentifier" : "MIR:00000396",
      "uris" : [ "urn:miriam:caps", "http://identifiers.org/caps/", "http://identifiers.org/caps", "https://identifiers.org/caps/", "https://identifiers.org/caps" ]
    },
    "CAS" : {
      "commonName" : "Chemical Abstracts Service",
      "homepage" : "http://commonchemistry.org",
      "registryIdentifier" : "MIR:00000237",
      "uris" : [ "urn:miriam:cas", "http://identifiers.org/cas/", "http://identifiers.org/cas", "https://identifiers.org/cas/", "https://identifiers.org/cas" ]
    },
    "CATH_DOMAIN" : {
      "commonName" : "CATH domain",
      "homepage" : "http://www.cathdb.info/",
      "registryIdentifier" : "MIR:00000210",
      "uris" : [ "urn:miriam:cath.domain", "http://identifiers.org/cath.domain/", "http://identifiers.org/cath.domain", "https://identifiers.org/cath.domain/", "https://identifiers.org/cath.domain" ]
    },
    "CATH_SUPERFAMILY" : {
      "commonName" : "CATH superfamily",
      "homepage" : "http://www.cathdb.info/",
      "registryIdentifier" : "MIR:00000209",
      "uris" : [ "urn:miriam:cath.superfamily", "http://identifiers.org/cath.superfamily/", "http://identifiers.org/cath.superfamily", "https://identifiers.org/cath.superfamily/", "https://identifiers.org/cath.superfamily" ]
    },
    "CAZY" : {
      "commonName" : "CAZy",
      "homepage" : "http://commonchemistry.org",
      "registryIdentifier" : "MIR:00000195",
      "uris" : [ "urn:miriam:cazy", "http://identifiers.org/cazy/", "http://identifiers.org/cazy", "https://identifiers.org/cazy/", "https://identifiers.org/cazy" ]
    },
    "CCDS" : {
      "commonName" : "Consensus CDS",
      "homepage" : "http://www.ncbi.nlm.nih.gov/CCDS/",
      "registryIdentifier" : "MIR:00000375",
      "uris" : [ "urn:miriam:ccds", "http://identifiers.org/ccds/", "http://identifiers.org/ccds", "https://identifiers.org/ccds/", "https://identifiers.org/ccds" ]
    },
    "CELL_CYCLE_ONTOLOGY" : {
      "commonName" : "Cell Cycle Ontology",
      "homepage" : "https://www.ebi.ac.uk/ontology-lookup/browse.do?ontName=CCO",
      "registryIdentifier" : "MIR:00000234",
      "uris" : [ "urn:miriam:cco", "http://identifiers.org/cco/", "http://identifiers.org/CCO", "https://identifiers.org/cco/", "https://identifiers.org/CCO" ]
    },
    "CELL_IMAGE_LIBRARY" : {
      "commonName" : "Cell Image Library",
      "homepage" : "http://cellimagelibrary.org/",
      "registryIdentifier" : "MIR:00000257",
      "uris" : [ "urn:miriam:cellimage", "http://identifiers.org/cellimage/", "http://identifiers.org/cellimage", "https://identifiers.org/cellimage/", "https://identifiers.org/cellimage" ]
    },
    "CELL_SIGNALING_TECHNOLOGY_ANTIBODY" : {
      "commonName" : "Cell Signaling Technology Antibody",
      "homepage" : "http://www.cellsignal.com/catalog/index.html",
      "registryIdentifier" : "MIR:00000430",
      "uris" : [ "urn:miriam:cst.ab", "http://identifiers.org/cst.ab/", "http://identifiers.org/cst.ab", "https://identifiers.org/cst.ab/", "https://identifiers.org/cst.ab" ]
    },
    "CELL_SIGNALING_TECHNOLOGY_PATHWAYS" : {
      "commonName" : "Cell Signaling Technology Pathways",
      "homepage" : "http://www.cellsignal.com/pathways/index.html",
      "registryIdentifier" : "MIR:00000429",
      "uris" : [ "urn:miriam:cst", "http://identifiers.org/cst/", "http://identifiers.org/cst", "https://identifiers.org/cst/", "https://identifiers.org/cst" ]
    },
    "CELL_TYPE_ONTOLOGY" : {
      "commonName" : "Cell Type Ontology",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/cl",
      "registryIdentifier" : "MIR:00000110",
      "uris" : [ "urn:miriam:cl", "urn:miriam:obo.clo", "http://identifiers.org/cl/", "http://identifiers.org/CL", "https://identifiers.org/cl/", "https://identifiers.org/CL" ]
    },
    "CGSC_STRAIN" : {
      "commonName" : "CGSC Strain",
      "homepage" : "http://cgsc.biology.yale.edu/index.php",
      "registryIdentifier" : "MIR:00000295",
      "uris" : [ "urn:miriam:cgsc", "http://identifiers.org/cgsc/", "http://identifiers.org/cgsc", "https://identifiers.org/cgsc/", "https://identifiers.org/cgsc" ]
    },
    "CHARPROT" : {
      "commonName" : "CharProt",
      "homepage" : "http://www.jcvi.org/charprotdb",
      "registryIdentifier" : "MIR:00000341",
      "uris" : [ "urn:miriam:charprot", "http://identifiers.org/charprot/", "http://identifiers.org/charprot", "https://identifiers.org/charprot/", "https://identifiers.org/charprot" ]
    },
    "CHEBI" : {
      "commonName" : "Chebi",
      "homepage" : "http://www.ebi.ac.uk/chebi/",
      "registryIdentifier" : "MIR:00000002",
      "uris" : [ "urn:miriam:obo.chebi", "urn:miriam:chebi", "http://identifiers.org/chebi/", "http://identifiers.org/obo.chebi/", "http://identifiers.org/CHEBI", "https://identifiers.org/chebi/", "https://identifiers.org/obo.chebi/", "https://identifiers.org/CHEBI" ]
    },
    "CHEMBL_COMPOUND" : {
      "commonName" : "ChEMBL",
      "homepage" : "https://www.ebi.ac.uk/chembldb/",
      "registryIdentifier" : "MIR:00000084",
      "uris" : [ "urn:miriam:chembl.compound", "http://identifiers.org/chembl.compound/", "http://identifiers.org/chembl.compound", "https://identifiers.org/chembl.compound/", "https://identifiers.org/chembl.compound" ]
    },
    "CHEMBL_TARGET" : {
      "commonName" : "ChEMBL target",
      "homepage" : "https://www.ebi.ac.uk/chembldb/",
      "registryIdentifier" : "MIR:00000085",
      "uris" : [ "urn:miriam:chembl.target", "http://identifiers.org/chembl.target/", "http://identifiers.org/chembl.target", "https://identifiers.org/chembl.target/", "https://identifiers.org/chembl.target" ]
    },
    "CHEMDB" : {
      "commonName" : "ChemDB",
      "homepage" : "http://cdb.ics.uci.edu/",
      "registryIdentifier" : "MIR:00000279",
      "uris" : [ "urn:miriam:chemdb", "http://identifiers.org/chemdb/", "http://identifiers.org/chemdb", "https://identifiers.org/chemdb/", "https://identifiers.org/chemdb" ]
    },
    "CHEMSPIDER" : {
      "commonName" : "ChemSpider",
      "homepage" : "http://www.chemspider.com/",
      "registryIdentifier" : "MIR:00000138",
      "uris" : [ "urn:miriam:chemspider", "http://identifiers.org/chemspider/", "http://identifiers.org/chemspider", "https://identifiers.org/chemspider/", "https://identifiers.org/chemspider" ]
    },
    "CHEM_ID_PLUS" : {
      "commonName" : "ChemIDplus",
      "homepage" : "https://chem.nlm.nih.gov/chemidplus/",
      "registryIdentifier" : "MIR:00000096",
      "uris" : [ "urn:miriam:chemidplus", "http://identifiers.org/chemidplus/", "http://identifiers.org/chemidplus", "https://identifiers.org/chemidplus/", "https://identifiers.org/chemidplus" ]
    },
    "CLDB" : {
      "commonName" : "CLDB",
      "homepage" : "http://bioinformatics.hsanmartino.it/hypercldb/indexes.html",
      "registryIdentifier" : "MIR:00000390",
      "uris" : [ "urn:miriam:cldb", "http://identifiers.org/cldb/", "http://identifiers.org/cldb", "https://identifiers.org/cldb/", "https://identifiers.org/cldb" ]
    },
    "CLINICAL_TRIALS_GOV" : {
      "commonName" : "ClinicalTrials.gov",
      "homepage" : "https://clinicaltrials.gov/",
      "registryIdentifier" : "MIR:00000137",
      "uris" : [ "urn:miriam:clinicaltrials", "http://identifiers.org/clinicaltrials/", "http://identifiers.org/clinicaltrials", "https://identifiers.org/clinicaltrials/", "https://identifiers.org/clinicaltrials" ]
    },
    "CLINVAR_RECORD" : {
      "commonName" : "ClinVar Record",
      "homepage" : "http://www.ncbi.nlm.nih.gov/clinvar/",
      "registryIdentifier" : "MIR:00000534",
      "uris" : [ "urn:miriam:clinvar.record", "http://identifiers.org/clinvar.record/", "http://identifiers.org/clinvar.record", "https://identifiers.org/clinvar.record/", "https://identifiers.org/clinvar.record" ]
    },
    "COG" : {
      "commonName" : "Clusters of Orthologous Groups",
      "homepage" : "https://www.ncbi.nlm.nih.gov/COG/",
      "registryIdentifier" : "MIR:00000296",
      "uris" : [ "urn:miriam:cogs" ]
    },
    "COMBINE_SPECIFICATIONS" : {
      "commonName" : "COMBINE specifications",
      "homepage" : "https://co.mbine.org/standards/",
      "registryIdentifier" : "MIR:00000258",
      "uris" : [ "urn:miriam:combine.specifications", "http://identifiers.org/combine.specifications/", "http://identifiers.org/combine.specifications", "https://identifiers.org/combine.specifications/", "https://identifiers.org/combine.specifications" ]
    },
    "COMPLEX_PORTAL" : {
      "commonName" : "Complex Portal",
      "homepage" : "https://www.ebi.ac.uk/complexportal",
      "registryIdentifier" : "MIR:00000657",
      "uris" : [ "https://identifiers.org/complexportal", "https://identifiers.org/complexportal/", "http://identifiers.org/complexportal", "http://identifiers.org/complexportal/" ]
    },
    "COMPULYEAST" : {
      "commonName" : "Compulyeast",
      "homepage" : "http://compluyeast2dpage.dacya.ucm.es/",
      "registryIdentifier" : "MIR:00000198",
      "uris" : [ "urn:miriam:compulyeast", "http://identifiers.org/compulyeast/", "http://identifiers.org/compulyeast", "https://identifiers.org/compulyeast/", "https://identifiers.org/compulyeast" ]
    },
    "CONOSERVER" : {
      "commonName" : "Conoserver",
      "homepage" : "http://www.conoserver.org/",
      "registryIdentifier" : "MIR:00000254",
      "uris" : [ "urn:miriam:conoserver", "http://identifiers.org/conoserver/", "http://identifiers.org/conoserver", "https://identifiers.org/conoserver/", "https://identifiers.org/conoserver" ]
    },
    "CONSERVED_DOMAIN_DATABASE" : {
      "commonName" : "Conserved Domain Database",
      "homepage" : "https://www.ncbi.nlm.nih.gov/sites/entrez?db=cdd",
      "registryIdentifier" : "MIR:00000119",
      "uris" : [ "urn:miriam:cdd", "http://identifiers.org/cdd/", "http://identifiers.org/cdd", "https://identifiers.org/cdd/", "https://identifiers.org/cdd" ]
    },
    "CORIELL_CELL_REPOSITORIES" : {
      "commonName" : "Coriell Cell Repositories",
      "homepage" : "http://ccr.coriell.org/",
      "registryIdentifier" : "MIR:00000439",
      "uris" : [ "urn:miriam:coriell", "http://identifiers.org/coriell/", "http://identifiers.org/coriell", "https://identifiers.org/coriell/", "https://identifiers.org/coriell" ]
    },
    "CORUM" : {
      "commonName" : "CORUM",
      "homepage" : "https://mips.helmholtz-muenchen.de/genre/proj/corum/",
      "registryIdentifier" : "MIR:00000440",
      "uris" : [ "urn:miriam:corum", "http://identifiers.org/corum/", "http://identifiers.org/corum", "https://identifiers.org/corum/", "https://identifiers.org/corum" ]
    },
    "CPC" : {
      "commonName" : "Cooperative Patent Classification",
      "homepage" : "https://worldwide.espacenet.com/classification",
      "registryIdentifier" : "MIR:00000539",
      "uris" : [ "urn:miriam:cpc", "https://identifiers.org/cpc", "https://identifiers.org/cpc/", "http://identifiers.org/cpc", "http://identifiers.org/cpc/" ]
    },
    "CRYPTODB" : {
      "commonName" : "CryptoDB",
      "homepage" : "https://cryptodb.org/cryptodb/",
      "registryIdentifier" : "MIR:00000149",
      "uris" : [ "urn:miriam:cryptodb", "http://identifiers.org/cryptodb/", "http://identifiers.org/cryptodb", "https://identifiers.org/cryptodb/", "https://identifiers.org/cryptodb" ]
    },
    "CSA" : {
      "commonName" : "CSA",
      "homepage" : "https://www.ebi.ac.uk/thornton-srv/databases/CSA/",
      "registryIdentifier" : "MIR:00000144",
      "uris" : [ "urn:miriam:csa", "http://identifiers.org/csa/", "http://identifiers.org/csa", "https://identifiers.org/csa/", "https://identifiers.org/csa" ]
    },
    "CTD_DISEASE" : {
      "commonName" : "CTD Disease",
      "homepage" : "http://ctdbase.org/",
      "registryIdentifier" : "MIR:00000099",
      "uris" : [ "urn:miriam:ctd.disease", "http://identifiers.org/ctd.disease/", "http://identifiers.org/ctd.disease", "https://identifiers.org/ctd.disease/", "https://identifiers.org/ctd.disease" ]
    },
    "CTD_GENE" : {
      "commonName" : "CTD Gene",
      "homepage" : "http://ctdbase.org/",
      "registryIdentifier" : "MIR:00000100",
      "uris" : [ "urn:miriam:ctd.gene", "http://identifiers.org/ctd.gene/", "http://identifiers.org/ctd.gene", "https://identifiers.org/ctd.gene/", "https://identifiers.org/ctd.gene" ]
    },
    "CUBE_DB" : {
      "commonName" : "Cube db",
      "homepage" : "http://epsf.bmad.bii.a-star.edu.sg/cube/db/html/home.html",
      "registryIdentifier" : "MIR:00000397",
      "uris" : [ "urn:miriam:cubedb", "http://identifiers.org/cubedb/", "http://identifiers.org/cubedb", "https://identifiers.org/cubedb/", "https://identifiers.org/cubedb" ]
    },
    "CUTDB" : {
      "commonName" : "CutDB",
      "homepage" : "http://cutdb.burnham.org",
      "registryIdentifier" : "MIR:00000225",
      "uris" : [ "urn:miriam:pmap.cutdb", "http://identifiers.org/pmap.cutdb/", "http://identifiers.org/pmap.cutdb", "https://identifiers.org/pmap.cutdb/", "https://identifiers.org/pmap.cutdb" ]
    },
    "DAILYMED" : {
      "commonName" : "DailyMed",
      "homepage" : "https://dailymed.nlm.nih.gov/dailymed/",
      "registryIdentifier" : "MIR:00000434",
      "uris" : [ "urn:miriam:dailymed", "http://identifiers.org/dailymed/", "http://identifiers.org/dailymed", "https://identifiers.org/dailymed/", "https://identifiers.org/dailymed" ]
    },
    "DARC" : {
      "commonName" : "DARC",
      "homepage" : "http://darcsite.genzentrum.lmu.de/darc/index.php",
      "registryIdentifier" : "MIR:00000366",
      "uris" : [ "urn:miriam:darc", "http://identifiers.org/darc/", "http://identifiers.org/darc", "https://identifiers.org/darc/", "https://identifiers.org/darc" ]
    },
    "DATABASE_OF_INTERACTING_PROTEINS" : {
      "commonName" : "Database of Interacting Proteins",
      "homepage" : "https://dip.doe-mbi.ucla.edu/",
      "registryIdentifier" : "MIR:00000044",
      "uris" : [ "urn:miriam:dip", "http://identifiers.org/dip/", "http://identifiers.org/dip", "https://identifiers.org/dip/", "https://identifiers.org/dip" ]
    },
    "DATABASE_OF_QUANTITATIVE_CELLULAR_SIGNALING_MODEL" : {
      "commonName" : "Database of Quantitative Cellular Signaling: Model",
      "homepage" : "http://doqcs.ncbs.res.in/",
      "registryIdentifier" : "MIR:00000134",
      "uris" : [ "urn:miriam:doqcs.model", "http://identifiers.org/doqcs.model/", "http://identifiers.org/doqcs.model", "https://identifiers.org/doqcs.model/", "https://identifiers.org/doqcs.model" ]
    },
    "DATABASE_OF_QUANTITATIVE_CELLULAR_SIGNALING_PATHWAY" : {
      "commonName" : "Database of Quantitative Cellular Signaling: Pathway",
      "homepage" : "http://doqcs.ncbs.res.in/",
      "registryIdentifier" : "MIR:00000135",
      "uris" : [ "urn:miriam:doqcs.pathway", "http://identifiers.org/doqcs.pathway/", "http://identifiers.org/doqcs.pathway", "https://identifiers.org/doqcs.pathway/", "https://identifiers.org/doqcs.pathway" ]
    },
    "DATF" : {
      "commonName" : "DATF",
      "homepage" : "http://datf.cbi.pku.edu.cn/",
      "registryIdentifier" : "MIR:00000456",
      "uris" : [ "urn:miriam:datf", "http://identifiers.org/datf/", "http://identifiers.org/datf", "https://identifiers.org/datf/", "https://identifiers.org/datf" ]
    },
    "DBD" : {
      "commonName" : "DBD",
      "homepage" : "http://www.transcriptionfactor.org/",
      "registryIdentifier" : "MIR:00000455",
      "uris" : [ "urn:miriam:dbd", "http://identifiers.org/dbd/", "http://identifiers.org/dbd", "https://identifiers.org/dbd/", "https://identifiers.org/dbd" ]
    },
    "DBEST" : {
      "commonName" : "dbEST",
      "homepage" : "https://www.ncbi.nlm.nih.gov/nucest",
      "registryIdentifier" : "MIR:00000159",
      "uris" : [ "urn:miriam:dbest", "http://identifiers.org/dbest/", "http://identifiers.org/dbest", "https://identifiers.org/dbest/", "https://identifiers.org/dbest" ]
    },
    "DBG2_INTRONS" : {
      "commonName" : "DBG2 Introns",
      "homepage" : "http://webapps2.ucalgary.ca/~groupii/",
      "registryIdentifier" : "MIR:00000318",
      "uris" : [ "urn:miriam:dbg2introns", "http://identifiers.org/dbg2introns/", "http://identifiers.org/dbg2introns", "https://identifiers.org/dbg2introns/", "https://identifiers.org/dbg2introns" ]
    },
    "DBPROBE" : {
      "commonName" : "dbProbe",
      "homepage" : "https://www.ncbi.nlm.nih.gov/sites/entrez?db=probe",
      "registryIdentifier" : "MIR:00000160",
      "uris" : [ "urn:miriam:dbprobe", "http://identifiers.org/dbprobe/", "http://identifiers.org/dbprobe", "https://identifiers.org/dbprobe/", "https://identifiers.org/dbprobe" ]
    },
    "DB_SNP" : {
      "commonName" : "dbSNP at NCBI",
      "homepage" : "https://www.ncbi.nlm.nih.gov/snp/",
      "registryIdentifier" : "MIR:00000161",
      "uris" : [ "urn:miriam:dbsnp", "http://identifiers.org/dbsnp/", "http://identifiers.org/dbsnp", "https://identifiers.org/dbsnp/", "https://identifiers.org/dbsnp" ]
    },
    "DEGRADOME_DATABASE" : {
      "commonName" : "Degradome Database",
      "homepage" : "http://degradome.uniovi.es/",
      "registryIdentifier" : "MIR:00000454",
      "uris" : [ "urn:miriam:degradome", "http://identifiers.org/degradome/", "http://identifiers.org/degradome", "https://identifiers.org/degradome/", "https://identifiers.org/degradome" ]
    },
    "DEPOD" : {
      "commonName" : "DEPOD",
      "homepage" : "http://www.depod.bioss.uni-freiburg.de",
      "registryIdentifier" : "MIR:00000428",
      "uris" : [ "urn:miriam:depod", "http://identifiers.org/depod/", "http://identifiers.org/depod", "https://identifiers.org/depod/", "https://identifiers.org/depod" ]
    },
    "DICTYBASE_EST" : {
      "commonName" : "Dictybase EST",
      "homepage" : "http://dictybase.org/",
      "registryIdentifier" : "MIR:00000330",
      "uris" : [ "urn:miriam:dictybase.est", "http://identifiers.org/dictybase.est/", "http://identifiers.org/dictybase.est", "https://identifiers.org/dictybase.est/", "https://identifiers.org/dictybase.est" ]
    },
    "DICTYBASE_GENE" : {
      "commonName" : "Dictybase Gene",
      "homepage" : "http://dictybase.org/",
      "registryIdentifier" : "MIR:00000286",
      "uris" : [ "urn:miriam:dictybase.gene", "http://identifiers.org/dictybase.gene/", "http://identifiers.org/dictybase.gene", "https://identifiers.org/dictybase.gene/", "https://identifiers.org/dictybase.gene" ]
    },
    "DISPROT" : {
      "commonName" : "DisProt",
      "homepage" : "https://disprot.org/",
      "registryIdentifier" : "MIR:00000199",
      "uris" : [ "urn:miriam:disprot", "http://identifiers.org/disprot/", "http://identifiers.org/disprot", "https://identifiers.org/disprot/", "https://identifiers.org/disprot" ]
    },
    "DOI" : {
      "commonName" : "Digital Object Identifier",
      "homepage" : "http://www.doi.org/",
      "registryIdentifier" : "MIR:00000019",
      "uris" : [ "urn:miriam:doi", "http://identifiers.org/doi/", "http://identifiers.org/doi", "https://identifiers.org/doi/", "https://identifiers.org/doi" ]
    },
    "DOMMINO" : {
      "commonName" : "DOMMINO",
      "homepage" : "http://dommino.org/",
      "registryIdentifier" : "MIR:00000373",
      "uris" : [ "urn:miriam:dommino", "http://identifiers.org/dommino/", "http://identifiers.org/dommino", "https://identifiers.org/dommino/", "https://identifiers.org/dommino" ]
    },
    "DOOR" : {
      "commonName" : "DOOR",
      "homepage" : "http://csbl.bmb.uga.edu/DOOR/operon.php",
      "registryIdentifier" : "MIR:00000453",
      "uris" : [ "urn:miriam:door", "http://identifiers.org/door/", "http://identifiers.org/door", "https://identifiers.org/door/", "https://identifiers.org/door" ]
    },
    "DPV" : {
      "commonName" : "DPV",
      "homepage" : "http://www.dpvweb.net/",
      "registryIdentifier" : "MIR:00000280",
      "uris" : [ "urn:miriam:dpv", "http://identifiers.org/dpv/", "http://identifiers.org/dpv", "https://identifiers.org/dpv/", "https://identifiers.org/dpv" ]
    },
    "DRAGONDB_ALLELE" : {
      "commonName" : "DragonDB Allele",
      "homepage" : "http://www.antirrhinum.net/",
      "registryIdentifier" : "MIR:00000300",
      "uris" : [ "urn:miriam:dragondb.allele", "http://identifiers.org/dragondb.allele/", "http://identifiers.org/dragondb.allele", "https://identifiers.org/dragondb.allele/", "https://identifiers.org/dragondb.allele" ]
    },
    "DRAGONDB_DNA" : {
      "commonName" : "DragonDB DNA",
      "homepage" : "http://www.antirrhinum.net/",
      "registryIdentifier" : "MIR:00000297",
      "uris" : [ "urn:miriam:dragondb.dna", "http://identifiers.org/dragondb.dna/", "http://identifiers.org/dragondb.dna", "https://identifiers.org/dragondb.dna/", "https://identifiers.org/dragondb.dna" ]
    },
    "DRAGONDB_LOCUS" : {
      "commonName" : "DragonDB Locus",
      "homepage" : "http://www.antirrhinum.net/",
      "registryIdentifier" : "MIR:00000299",
      "uris" : [ "urn:miriam:dragondb.locus", "http://identifiers.org/dragondb.locus/", "http://identifiers.org/dragondb.locus", "https://identifiers.org/dragondb.locus/", "https://identifiers.org/dragondb.locus" ]
    },
    "DRAGONDB_PROTEIN" : {
      "commonName" : "DragonDB Protein",
      "homepage" : "http://www.antirrhinum.net/",
      "registryIdentifier" : "MIR:00000298",
      "uris" : [ "urn:miriam:dragondb.protein", "http://identifiers.org/dragondb.protein/", "http://identifiers.org/dragondb.protein", "https://identifiers.org/dragondb.protein/", "https://identifiers.org/dragondb.protein" ]
    },
    "DRSC" : {
      "commonName" : "DRSC",
      "homepage" : "http://flyrnai.org/",
      "registryIdentifier" : "MIR:00000367",
      "uris" : [ "urn:miriam:drsc", "http://identifiers.org/drsc/", "http://identifiers.org/drsc", "https://identifiers.org/drsc/", "https://identifiers.org/drsc" ]
    },
    "DRUGBANK" : {
      "commonName" : "DrugBank",
      "homepage" : "http://www.drugbank.ca/",
      "registryIdentifier" : "MIR:00000102",
      "uris" : [ "urn:miriam:drugbank", "http://identifiers.org/drugbank/", "http://identifiers.org/drugbank", "https://identifiers.org/drugbank/", "https://identifiers.org/drugbank" ]
    },
    "DRUGBANK_TARGET_V4" : {
      "commonName" : "DrugBank Target v4",
      "homepage" : "http://www.drugbank.ca/targets",
      "registryIdentifier" : "MIR:00000528",
      "uris" : [ "urn:miriam:drugbankv4.target", "urn:miriam:drugbank.target", "http://identifiers.org/drugbankv4.target/", "http://identifiers.org/drugbankv4.target", "https://identifiers.org/drugbankv4.target/", "https://identifiers.org/drugbankv4.target" ]
    },
    "EC" : {
      "commonName" : "Enzyme Nomenclature",
      "homepage" : "http://www.enzyme-database.org/",
      "registryIdentifier" : "MIR:00000004",
      "uris" : [ "urn:miriam:ec-code", "urn:lsid:ec-code.org", "http://identifiers.org/ec-code/", "http://identifiers.org/ec-code", "https://identifiers.org/ec-code/", "https://identifiers.org/ec-code" ]
    },
    "ECHOBASE" : {
      "commonName" : "EchoBASE",
      "homepage" : "http://www.york.ac.uk/",
      "registryIdentifier" : "MIR:00000200",
      "uris" : [ "urn:miriam:echobase", "http://identifiers.org/echobase/", "http://identifiers.org/echobase", "https://identifiers.org/echobase/", "https://identifiers.org/echobase" ]
    },
    "ECO" : {
      "commonName" : "Evidence Code Ontology",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/eco",
      "registryIdentifier" : "MIR:00000055",
      "uris" : [ "urn:miriam:obo.eco", "urn:miriam:eco", "http://identifiers.org/eco/", "http://identifiers.org/obo.eco/", "http://identifiers.org/ECO", "https://identifiers.org/eco/", "https://identifiers.org/obo.eco/", "https://identifiers.org/ECO" ]
    },
    "ECOGENE" : {
      "commonName" : "EcoGene",
      "homepage" : "http://ecogene.org/",
      "registryIdentifier" : "MIR:00000163",
      "uris" : [ "urn:miriam:ecogene", "http://identifiers.org/ecogene/", "http://identifiers.org/ecogene", "https://identifiers.org/ecogene/", "https://identifiers.org/ecogene" ]
    },
    "ECOLIWIKI" : {
      "commonName" : "EcoliWiki",
      "homepage" : "http://ecoliwiki.net/colipedia/",
      "registryIdentifier" : "MIR:00000442",
      "uris" : [ "urn:miriam:ecoliwiki", "http://identifiers.org/ecoliwiki/", "http://identifiers.org/ecoliwiki", "https://identifiers.org/ecoliwiki/", "https://identifiers.org/ecoliwiki" ]
    },
    "EDAM_ONTOLOGY" : {
      "commonName" : "EDAM Ontology",
      "homepage" : "http://bioportal.bioontology.org/ontologies/EDAM",
      "registryIdentifier" : "MIR:00000189",
      "uris" : [ "urn:miriam:edam", "http://identifiers.org/edam/", "http://identifiers.org/edam", "https://identifiers.org/edam/", "https://identifiers.org/edam" ]
    },
    "EGGNOG" : {
      "commonName" : "eggNOG",
      "homepage" : "http://eggnog.embl.de/version_3.0/",
      "registryIdentifier" : "MIR:00000201",
      "uris" : [ "urn:miriam:eggnog", "http://identifiers.org/eggnog/", "http://identifiers.org/eggnog", "https://identifiers.org/eggnog/", "https://identifiers.org/eggnog" ]
    },
    "ELM" : {
      "commonName" : "ELM",
      "homepage" : "http://elm.eu.org/",
      "registryIdentifier" : "MIR:00000250",
      "uris" : [ "urn:miriam:elm", "http://identifiers.org/elm/", "http://identifiers.org/elm", "https://identifiers.org/elm/", "https://identifiers.org/elm" ]
    },
    "ENA" : {
      "commonName" : "ENA",
      "homepage" : "https://www.ncbi.nlm.nih.gov/Genbank/",
      "registryIdentifier" : "MIR:00000372",
      "uris" : [ "urn:miriam:ena.embl", "http://identifiers.org/ena.embl/", "http://identifiers.org/ena.embl", "https://identifiers.org/ena.embl/", "https://identifiers.org/ena.embl" ]
    },
    "ENSEMBL" : {
      "commonName" : "Ensembl",
      "homepage" : "https://www.ensembl.org/",
      "registryIdentifier" : "MIR:00000003",
      "uris" : [ "urn:miriam:ensembl", "http://identifiers.org/ensembl/", "http://identifiers.org/ensembl.gene/", "http://identifiers.org/ensembl", "https://identifiers.org/ensembl/", "https://identifiers.org/ensembl.gene/", "https://identifiers.org/ensembl" ]
    },
    "ENSEMBL_BACTERIA" : {
      "commonName" : "Ensembl Bacteria",
      "homepage" : "https://bacteria.ensembl.org/",
      "registryIdentifier" : "MIR:00000202",
      "uris" : [ "urn:miriam:ensembl.bacteria", "http://identifiers.org/ensembl.bacteria/", "http://identifiers.org/ensembl.bacteria", "https://identifiers.org/ensembl.bacteria/", "https://identifiers.org/ensembl.bacteria" ]
    },
    "ENSEMBL_FUNGI" : {
      "commonName" : "Ensembl Fungi",
      "homepage" : "https://fungi.ensembl.org/",
      "registryIdentifier" : "MIR:00000206",
      "uris" : [ "urn:miriam:ensembl.fungi", "http://identifiers.org/ensembl.fungi/", "http://identifiers.org/ensembl.fungi", "https://identifiers.org/ensembl.fungi/", "https://identifiers.org/ensembl.fungi" ]
    },
    "ENSEMBL_METAZOA" : {
      "commonName" : "Ensembl Metazoa",
      "homepage" : "https://metazoa.ensembl.org/",
      "registryIdentifier" : "MIR:00000204",
      "uris" : [ "urn:miriam:ensembl.metazoa", "http://identifiers.org/ensembl.metazoa/", "http://identifiers.org/ensembl.metazoa", "https://identifiers.org/ensembl.metazoa/", "https://identifiers.org/ensembl.metazoa" ]
    },
    "ENSEMBL_PLANTS" : {
      "commonName" : "Ensembl Plants",
      "homepage" : "http://plants.ensembl.org/",
      "registryIdentifier" : "MIR:00000205",
      "uris" : [ "urn:miriam:ensembl.plant", "http://identifiers.org/ensembl.plant/", "http://identifiers.org/ensembl.plant", "https://identifiers.org/ensembl.plant/", "https://identifiers.org/ensembl.plant" ]
    },
    "ENSEMBL_PROTISTS" : {
      "commonName" : "Ensembl Protists",
      "homepage" : "https://protists.ensembl.org",
      "registryIdentifier" : "MIR:00000203",
      "uris" : [ "urn:miriam:ensembl.protist", "http://identifiers.org/ensembl.protist/", "http://identifiers.org/ensembl.protist", "https://identifiers.org/ensembl.protist/", "https://identifiers.org/ensembl.protist" ]
    },
    "ENTREZ" : {
      "commonName" : "Entrez Gene",
      "homepage" : "http://www.ncbi.nlm.nih.gov/gene",
      "registryIdentifier" : "MIR:00000069",
      "uris" : [ "urn:miriam:ncbigene", "urn:miriam:ncbi.gene", "urn:miriam:entrez.gene", "http://identifiers.org/ncbigene/", "http://identifiers.org/ncbigene", "https://identifiers.org/ncbigene/", "https://identifiers.org/ncbigene" ]
    },
    "ENVIPATH" : {
      "commonName" : "enviPath",
      "homepage" : "https://envipath.org/",
      "registryIdentifier" : "MIR:00000727",
      "uris" : [ "http://identifiers.org/envipath/", "http://identifiers.org/envipath", "https://identifiers.org/envipath/", "https://identifiers.org/envipath" ]
    },
    "EPD" : {
      "commonName" : "EPD",
      "homepage" : "http://epd.vital-it.ch/",
      "registryIdentifier" : "MIR:00000408",
      "uris" : [ "urn:miriam:epd", "http://identifiers.org/epd/", "http://identifiers.org/epd", "https://identifiers.org/epd/", "https://identifiers.org/epd" ]
    },
    "EUROPEAN_GENOME_PHENOME_ARCHIVE_DATASET" : {
      "commonName" : "European Genome-phenome Archive Dataset",
      "homepage" : "https://www.ebi.ac.uk/ega/dataset",
      "registryIdentifier" : "MIR:00000512",
      "uris" : [ "urn:miriam:ega.dataset", "http://identifiers.org/ega.dataset/", "http://identifiers.org/ega.dataset", "https://identifiers.org/ega.dataset/", "https://identifiers.org/ega.dataset" ]
    },
    "EUROPEAN_GENOME_PHENOME_ARCHIVE_STUDY" : {
      "commonName" : "European Genome-phenome Archive Study",
      "homepage" : "https://www.ebi.ac.uk/ega/studies",
      "registryIdentifier" : "MIR:00000511",
      "uris" : [ "urn:miriam:ega.study", "http://identifiers.org/ega.study/", "http://identifiers.org/ega.study", "https://identifiers.org/ega.study/", "https://identifiers.org/ega.study" ]
    },
    "EU_CLINICAL_TRIALS" : {
      "commonName" : "EU Clinical Trials",
      "homepage" : "https://www.clinicaltrialsregister.eu/",
      "registryIdentifier" : "MIR:00000536",
      "uris" : [ "urn:miriam:euclinicaltrials", "http://identifiers.org/euclinicaltrials/", "http://identifiers.org/euclinicaltrials", "https://identifiers.org/euclinicaltrials/", "https://identifiers.org/euclinicaltrials" ]
    },
    "EXAC_GENE" : {
      "commonName" : "ExAC Gene",
      "homepage" : "http://exac.broadinstitute.org/",
      "registryIdentifier" : "MIR:00000548",
      "uris" : [ "urn:miriam:exac.gene", "http://identifiers.org/exac.gene/", "http://identifiers.org/exac.gene", "https://identifiers.org/exac.gene/", "https://identifiers.org/exac.gene" ]
    },
    "EXAC_TRANSCRIPT" : {
      "commonName" : "ExAC Transcript",
      "homepage" : "http://exac.broadinstitute.org/",
      "registryIdentifier" : "MIR:00000547",
      "uris" : [ "urn:miriam:exac.transcript", "http://identifiers.org/exac.transcript/", "http://identifiers.org/exac.transcript", "https://identifiers.org/exac.transcript/", "https://identifiers.org/exac.transcript" ]
    },
    "EXAC_VARIANT" : {
      "commonName" : "ExAC Variant",
      "homepage" : "http://exac.broadinstitute.org/",
      "registryIdentifier" : "MIR:00000541",
      "uris" : [ "urn:miriam:exac.variant", "http://identifiers.org/exac.variant/", "http://identifiers.org/exac.variant", "https://identifiers.org/exac.variant/", "https://identifiers.org/exac.variant" ]
    },
    "EXPERIMENTAL_FACTOR_ONTOLOGY" : {
      "commonName" : "Experimental Factor Ontology",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/efo",
      "registryIdentifier" : "MIR:00000391",
      "uris" : [ "urn:miriam:efo", "http://identifiers.org/efo/", "http://identifiers.org/efo", "https://identifiers.org/efo/", "https://identifiers.org/efo" ]
    },
    "FLYBASE" : {
      "commonName" : "FlyBase",
      "homepage" : "https://www.alliancegenome.org",
      "registryIdentifier" : "MIR:00000030",
      "uris" : [ "urn:miriam:fb", "urn:miriam:flybase", "http://identifiers.org/fb/", "http://identifiers.org/fb", "https://identifiers.org/fb/", "https://identifiers.org/fb" ]
    },
    "FMA" : {
      "commonName" : "FMA",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/fma/",
      "registryIdentifier" : "MIR:00000067",
      "uris" : [ "urn:miriam:fma", "urn:miriam:obo.fma", "http://identifiers.org/fma/", "http://identifiers.org/FMA", "https://identifiers.org/fma/", "https://identifiers.org/FMA" ]
    },
    "FOODB_COMPOUND" : {
      "commonName" : "FooDB Compound",
      "homepage" : "http://foodb.ca/foods",
      "registryIdentifier" : "MIR:00000530",
      "uris" : [ "urn:miriam:foodb.compound", "http://identifiers.org/foodb.compound/", "http://identifiers.org/foodb.compound", "https://identifiers.org/foodb.compound/", "https://identifiers.org/foodb.compound" ]
    },
    "FUNCBASE_FLY" : {
      "commonName" : "FuncBase Fly",
      "homepage" : "http://func.mshri.on.ca/fly",
      "registryIdentifier" : "MIR:00000461",
      "uris" : [ "urn:miriam:funcbase.fly", "http://identifiers.org/funcbase.fly/", "http://identifiers.org/funcbase.fly", "https://identifiers.org/funcbase.fly/", "https://identifiers.org/funcbase.fly" ]
    },
    "FUNCBASE_HUMAN" : {
      "commonName" : "FuncBase Human",
      "homepage" : "http://func.mshri.on.ca/human/",
      "registryIdentifier" : "MIR:00000462",
      "uris" : [ "urn:miriam:funcbase.human", "http://identifiers.org/funcbase.human/", "http://identifiers.org/funcbase.human", "https://identifiers.org/funcbase.human/", "https://identifiers.org/funcbase.human" ]
    },
    "FUNCBASE_MOUSE" : {
      "commonName" : "FuncBase Mouse",
      "homepage" : "http://func.mshri.on.ca/mouse/",
      "registryIdentifier" : "MIR:00000463",
      "uris" : [ "urn:miriam:funcbase.mouse", "http://identifiers.org/funcbase.mouse/", "http://identifiers.org/funcbase.mouse", "https://identifiers.org/funcbase.mouse/", "https://identifiers.org/funcbase.mouse" ]
    },
    "FUNCBASE_YEAST" : {
      "commonName" : "FuncBase Yeast",
      "homepage" : "http://func.mshri.on.ca/yeast",
      "registryIdentifier" : "MIR:00000464",
      "uris" : [ "urn:miriam:funcbase.yeast", "http://identifiers.org/funcbase.yeast/", "http://identifiers.org/funcbase.yeast", "https://identifiers.org/funcbase.yeast/", "https://identifiers.org/funcbase.yeast" ]
    },
    "FUNGIDB" : {
      "commonName" : "FungiDB",
      "homepage" : "https://fungidb.org/fungidb",
      "registryIdentifier" : "MIR:00000365",
      "uris" : [ "urn:miriam:fungidb", "http://identifiers.org/fungidb/", "http://identifiers.org/fungidb", "https://identifiers.org/fungidb/", "https://identifiers.org/fungidb" ]
    },
    "F_SNP" : {
      "commonName" : "F-SNP",
      "homepage" : "http://compbio.cs.queensu.ca/F-SNP/",
      "registryIdentifier" : "MIR:00000496",
      "uris" : [ "urn:miriam:fsnp", "http://identifiers.org/fsnp/", "http://identifiers.org/fsnp", "https://identifiers.org/fsnp/", "https://identifiers.org/fsnp" ]
    },
    "GABI" : {
      "commonName" : "GABI",
      "homepage" : "http://www.gabipd.org/",
      "registryIdentifier" : "MIR:00000164",
      "uris" : [ "urn:miriam:gabi", "http://identifiers.org/gabi/", "http://identifiers.org/gabi", "https://identifiers.org/gabi/", "https://identifiers.org/gabi" ]
    },
    "GENATLAS" : {
      "commonName" : "Genatlas",
      "homepage" : "http://genatlas.medecine.univ-paris5.fr/",
      "registryIdentifier" : "MIR:00000208",
      "uris" : [ "urn:miriam:genatlas", "http://identifiers.org/genatlas/", "http://identifiers.org/genatlas", "https://identifiers.org/genatlas/", "https://identifiers.org/genatlas" ]
    },
    "GENECARDS" : {
      "commonName" : "GeneCards",
      "homepage" : "http://www.genecards.org/",
      "registryIdentifier" : "MIR:00000323",
      "uris" : [ "urn:miriam:genecards", "http://identifiers.org/genecards/", "http://identifiers.org/genecards", "https://identifiers.org/genecards/", "https://identifiers.org/genecards" ]
    },
    "GENEFARM" : {
      "commonName" : "GeneFarm",
      "homepage" : "http://urgi.versailles.inra.fr/Genefarm/",
      "registryIdentifier" : "MIR:00000211",
      "uris" : [ "urn:miriam:genefarm", "http://identifiers.org/genefarm/", "http://identifiers.org/genefarm", "https://identifiers.org/genefarm/", "https://identifiers.org/genefarm" ]
    },
    "GENETREE" : {
      "commonName" : "GeneTree",
      "homepage" : "http://www.ensembl.org/",
      "registryIdentifier" : "MIR:00000214",
      "uris" : [ "urn:miriam:genetree", "http://identifiers.org/genetree/", "http://identifiers.org/genetree", "https://identifiers.org/genetree/", "https://identifiers.org/genetree" ]
    },
    "GENE_DB" : {
      "commonName" : "GeneDB",
      "homepage" : "https://www.genedb.org/",
      "registryIdentifier" : "MIR:00000106",
      "uris" : [ "urn:miriam:genedb", "http://identifiers.org/genedb/", "http://identifiers.org/genedb", "https://identifiers.org/genedb/", "https://identifiers.org/genedb" ]
    },
    "GENE_WIKI" : {
      "commonName" : "Gene Wiki",
      "homepage" : "http://en.wikipedia.org/wiki/Gene_Wiki",
      "registryIdentifier" : "MIR:00000487",
      "uris" : [ "urn:miriam:genewiki", "http://identifiers.org/genewiki/", "http://identifiers.org/genewiki", "https://identifiers.org/genewiki/", "https://identifiers.org/genewiki" ]
    },
    "GENOME_PROPERTIES" : {
      "commonName" : "Genome Properties",
      "homepage" : "https://www.ebi.ac.uk/interpro/genomeproperties/",
      "registryIdentifier" : "MIR:00000443",
      "uris" : [ "urn:miriam:genprop", "http://identifiers.org/genprop/", "http://identifiers.org/genprop", "https://identifiers.org/genprop/", "https://identifiers.org/genprop" ]
    },
    "GENOMIC_DATA_COMMONS_DATA_PORTAL" : {
      "commonName" : "Genomic Data Commons Data Portal",
      "homepage" : "https://gdc.cancer.gov/",
      "registryIdentifier" : "MIR:00000604",
      "uris" : [ "http://identifiers.org/gdc/", "http://identifiers.org/gdc", "https://identifiers.org/gdc/", "https://identifiers.org/gdc" ]
    },
    "GENPEPT" : {
      "commonName" : "GenPept",
      "homepage" : "https://www.ncbi.nlm.nih.gov/protein",
      "registryIdentifier" : "MIR:00000345",
      "uris" : [ "urn:miriam:genpept", "http://identifiers.org/genpept/", "http://identifiers.org/genpept", "https://identifiers.org/genpept/", "https://identifiers.org/genpept" ]
    },
    "GEO" : {
      "commonName" : "GEO",
      "homepage" : "https://www.ncbi.nlm.nih.gov/geo/",
      "registryIdentifier" : "MIR:00000054",
      "uris" : [ "urn:miriam:geo", "http://identifiers.org/geo/", "http://identifiers.org/geo", "https://identifiers.org/geo/", "https://identifiers.org/geo" ]
    },
    "GIARDIADB" : {
      "commonName" : "GiardiaDB",
      "homepage" : "https://giardiadb.org/giardiadb/",
      "registryIdentifier" : "MIR:00000151",
      "uris" : [ "urn:miriam:giardiadb", "http://identifiers.org/giardiadb/", "http://identifiers.org/giardiadb", "https://identifiers.org/giardiadb/", "https://identifiers.org/giardiadb" ]
    },
    "GLIDA_GPCR" : {
      "commonName" : "GLIDA GPCR",
      "homepage" : "http://pharminfo.pharm.kyoto-u.ac.jp/services/glida/",
      "registryIdentifier" : "MIR:00000493",
      "uris" : [ "urn:miriam:glida.gpcr", "http://identifiers.org/glida.gpcr/", "http://identifiers.org/glida.gpcr", "https://identifiers.org/glida.gpcr/", "https://identifiers.org/glida.gpcr" ]
    },
    "GLIDA_LIGAND" : {
      "commonName" : "GLIDA Ligand",
      "homepage" : "http://pharminfo.pharm.kyoto-u.ac.jp/services/glida/",
      "registryIdentifier" : "MIR:00000494",
      "uris" : [ "urn:miriam:glida.ligand", "http://identifiers.org/glida.ligand/", "http://identifiers.org/glida.ligand", "https://identifiers.org/glida.ligand/", "https://identifiers.org/glida.ligand" ]
    },
    "GLYCOEPITOPE" : {
      "commonName" : "GlycoEpitope",
      "homepage" : "https://www.glycoepitope.jp/epitopes/",
      "registryIdentifier" : "MIR:00000478",
      "uris" : [ "urn:miriam:glycoepitope", "http://identifiers.org/glycoepitope/", "http://identifiers.org/glycoepitope", "https://identifiers.org/glycoepitope/", "https://identifiers.org/glycoepitope" ]
    },
    "GLYCOMEDB" : {
      "commonName" : "GlycomeDB",
      "homepage" : "https://glytoucan.org/",
      "registryIdentifier" : "MIR:00000114",
      "uris" : [ "urn:miriam:glycomedb", "http://identifiers.org/glycomedb/", "http://identifiers.org/glycomedb", "https://identifiers.org/glycomedb/", "https://identifiers.org/glycomedb" ]
    },
    "GO" : {
      "commonName" : "Gene Ontology",
      "homepage" : "http://amigo.geneontology.org/amigo",
      "registryIdentifier" : "MIR:00000022",
      "uris" : [ "urn:miriam:obo.go", "urn:miriam:go", "http://identifiers.org/go/", "http://identifiers.org/obo.go/", "http://identifiers.org/GO", "https://identifiers.org/go/", "https://identifiers.org/obo.go/", "https://identifiers.org/GO" ]
    },
    "GOA" : {
      "commonName" : "GOA",
      "homepage" : "https://www.ebi.ac.uk/GOA/",
      "registryIdentifier" : "MIR:00000196",
      "uris" : [ "urn:miriam:goa", "http://identifiers.org/goa/", "http://identifiers.org/goa", "https://identifiers.org/goa/", "https://identifiers.org/goa" ]
    },
    "GOLD_GENOME" : {
      "commonName" : "GOLD genome",
      "homepage" : "http://www.genomesonline.org/cgi-bin/GOLD/index.cgi",
      "registryIdentifier" : "MIR:00000401",
      "uris" : [ "urn:miriam:gold.genome", "http://identifiers.org/gold.genome/", "http://identifiers.org/gold.genome", "https://identifiers.org/gold.genome/", "https://identifiers.org/gold.genome" ]
    },
    "GOLD_METADATA" : {
      "commonName" : "GOLD metadata",
      "homepage" : "http://www.genomesonline.org/cgi-bin/GOLD/index.cgi",
      "registryIdentifier" : "MIR:00000402",
      "uris" : [ "urn:miriam:gold.meta", "http://identifiers.org/gold.meta/", "http://identifiers.org/gold.meta", "https://identifiers.org/gold.meta/", "https://identifiers.org/gold.meta" ]
    },
    "GOLM_METABOLOME_DATABASE" : {
      "commonName" : "Golm Metabolome Database",
      "homepage" : "http://gmd.mpimp-golm.mpg.de/",
      "registryIdentifier" : "MIR:00000274",
      "uris" : [ "urn:miriam:gmd", "http://identifiers.org/gmd/", "http://identifiers.org/gmd", "https://identifiers.org/gmd/", "https://identifiers.org/gmd" ]
    },
    "GOLM_METABOLOME_DATABASE_ANALYTE" : {
      "commonName" : "Golm Metabolome Database Analyte",
      "homepage" : "http://gmd.mpimp-golm.mpg.de/",
      "registryIdentifier" : "MIR:00000426",
      "uris" : [ "urn:miriam:gmd.analyte", "http://identifiers.org/gmd.analyte/", "http://identifiers.org/gmd.analyte", "https://identifiers.org/gmd.analyte/", "https://identifiers.org/gmd.analyte" ]
    },
    "GOLM_METABOLOME_DATABASE_GC_MS_SPECTRA" : {
      "commonName" : "Golm Metabolome Database GC-MS spectra",
      "homepage" : "http://gmd.mpimp-golm.mpg.de/",
      "registryIdentifier" : "MIR:00000424",
      "uris" : [ "urn:miriam:gmd.gcms", "http://identifiers.org/gmd.gcms/", "http://identifiers.org/gmd.gcms", "https://identifiers.org/gmd.gcms/", "https://identifiers.org/gmd.gcms" ]
    },
    "GOLM_METABOLOME_DATABASE_PROFILE" : {
      "commonName" : "Golm Metabolome Database Profile",
      "homepage" : "http://gmd.mpimp-golm.mpg.de/",
      "registryIdentifier" : "MIR:00000423",
      "uris" : [ "urn:miriam:gmd.profile", "http://identifiers.org/gmd.profile/", "http://identifiers.org/gmd.profile", "https://identifiers.org/gmd.profile/", "https://identifiers.org/gmd.profile" ]
    },
    "GOLM_METABOLOME_DATABASE_REFERENCE_SUBSTANCE" : {
      "commonName" : "Golm Metabolome Database Reference Substance",
      "homepage" : "http://gmd.mpimp-golm.mpg.de/",
      "registryIdentifier" : "MIR:00000425",
      "uris" : [ "urn:miriam:gmd.ref", "http://identifiers.org/gmd.ref/", "http://identifiers.org/gmd.ref", "https://identifiers.org/gmd.ref/", "https://identifiers.org/gmd.ref" ]
    },
    "GOOGLE_PATENTS" : {
      "commonName" : "Google Patents",
      "homepage" : "https://www.google.com/patents/",
      "registryIdentifier" : "MIR:00000537",
      "uris" : [ "urn:miriam:google.patent", "http://identifiers.org/google.patent/", "http://identifiers.org/google.patent", "https://identifiers.org/google.patent/", "https://identifiers.org/google.patent" ]
    },
    "GO_REF" : {
      "commonName" : "Gene Ontology Reference",
      "homepage" : "http://www.geneontology.org/cgi-bin/references.cgi",
      "registryIdentifier" : "MIR:00000450",
      "uris" : [ "urn:miriam:go.ref", "http://identifiers.org/GO_REF/", "http://identifiers.org/GO_REF", "https://identifiers.org/GO_REF/", "https://identifiers.org/GO_REF" ]
    },
    "GPCRDB" : {
      "commonName" : "GPCRDB",
      "homepage" : "http://www.gpcrdb.org/",
      "registryIdentifier" : "MIR:00000212",
      "uris" : [ "urn:miriam:gpcrdb", "http://identifiers.org/gpcrdb/", "http://identifiers.org/gpcrdb", "https://identifiers.org/gpcrdb/", "https://identifiers.org/gpcrdb" ]
    },
    "GRAMENE_GENES" : {
      "commonName" : "Gramene genes",
      "homepage" : "http://www.gramene.org/",
      "registryIdentifier" : "MIR:00000182",
      "uris" : [ "urn:miriam:gramene.gene", "http://identifiers.org/gramene.gene/", "http://identifiers.org/gramene.gene", "https://identifiers.org/gramene.gene/", "https://identifiers.org/gramene.gene" ]
    },
    "GRAMENE_PROTEIN" : {
      "commonName" : "Gramene protein",
      "homepage" : "http://www.gramene.org/",
      "registryIdentifier" : "MIR:00000181",
      "uris" : [ "urn:miriam:gramene.protein", "http://identifiers.org/gramene.protein/", "http://identifiers.org/gramene.protein", "https://identifiers.org/gramene.protein/", "https://identifiers.org/gramene.protein" ]
    },
    "GRAMENE_QTL" : {
      "commonName" : "Gramene QTL",
      "homepage" : "http://www.gramene.org/",
      "registryIdentifier" : "MIR:00000184",
      "uris" : [ "urn:miriam:gramene.qtl", "http://identifiers.org/gramene.qtl/", "http://identifiers.org/gramene.qtl", "https://identifiers.org/gramene.qtl/", "https://identifiers.org/gramene.qtl" ]
    },
    "GRAMENE_TAXONOMY" : {
      "commonName" : "Gramene Taxonomy",
      "homepage" : "http://www.gramene.org/",
      "registryIdentifier" : "MIR:00000183",
      "uris" : [ "urn:miriam:gramene.taxonomy", "http://identifiers.org/gramene.taxonomy/", "http://identifiers.org/gramene.taxonomy", "https://identifiers.org/gramene.taxonomy/", "https://identifiers.org/gramene.taxonomy" ]
    },
    "GREENGENES" : {
      "commonName" : "GreenGenes",
      "homepage" : "http://greengenes.lbl.gov/",
      "registryIdentifier" : "MIR:00000165",
      "uris" : [ "urn:miriam:greengenes", "http://identifiers.org/greengenes/", "http://identifiers.org/greengenes", "https://identifiers.org/greengenes/", "https://identifiers.org/greengenes" ]
    },
    "GRIN_PLANT_TAXONOMY" : {
      "commonName" : "GRIN Plant Taxonomy",
      "homepage" : "http://www.ars-grin.gov/cgi-bin/npgs/html/index.pl?language=en",
      "registryIdentifier" : "MIR:00000166",
      "uris" : [ "urn:miriam:grin.taxonomy", "http://identifiers.org/grin.taxonomy/", "http://identifiers.org/grin.taxonomy", "https://identifiers.org/grin.taxonomy/", "https://identifiers.org/grin.taxonomy" ]
    },
    "GRSDB" : {
      "commonName" : "GRSDB",
      "homepage" : "http://bioinformatics.ramapo.edu/GRSDB2/",
      "registryIdentifier" : "MIR:00000495",
      "uris" : [ "urn:miriam:grsdb", "http://identifiers.org/grsdb/", "http://identifiers.org/grsdb", "https://identifiers.org/grsdb/", "https://identifiers.org/grsdb" ]
    },
    "GWAS_CENRAL_MARKER" : {
      "commonName" : "GWAS Central Marker",
      "homepage" : "https://www.gwascentral.org/markers/",
      "registryIdentifier" : "MIR:00000542",
      "uris" : [ "urn:miriam:gwascentral.marker", "http://identifiers.org/gwascentral.marker/", "http://identifiers.org/gwascentral.marker", "https://identifiers.org/gwascentral.marker/", "https://identifiers.org/gwascentral.marker" ]
    },
    "GWAS_CENRAL_PHENOTYPE" : {
      "commonName" : "GWAS Central Phenotype",
      "homepage" : "https://www.gwascentral.org/phenotypes",
      "registryIdentifier" : "MIR:00000543",
      "uris" : [ "urn:miriam:gwascentral.phenotype", "http://identifiers.org/gwascentral.phenotype/", "http://identifiers.org/gwascentral.phenotype", "https://identifiers.org/gwascentral.phenotype/", "https://identifiers.org/gwascentral.phenotype" ]
    },
    "GWAS_CENRAL_STUDY" : {
      "commonName" : "GWAS Central Study",
      "homepage" : "https://www.gwascentral.org/studies",
      "registryIdentifier" : "MIR:00000540",
      "uris" : [ "urn:miriam:gwascentral.study", "http://identifiers.org/gwascentral.study/", "http://identifiers.org/gwascentral.study", "https://identifiers.org/gwascentral.study/", "https://identifiers.org/gwascentral.study" ]
    },
    "GXA_EXPT" : {
      "commonName" : "GXA Expt",
      "homepage" : "https://www.ebi.ac.uk/gxa/",
      "registryIdentifier" : "MIR:00000379",
      "uris" : [ "urn:miriam:gxa.expt", "http://identifiers.org/gxa.expt/", "http://identifiers.org/gxa.expt", "https://identifiers.org/gxa.expt/", "https://identifiers.org/gxa.expt" ]
    },
    "GXA_GENE" : {
      "commonName" : "GXA Gene",
      "homepage" : "https://www.ebi.ac.uk/gxa/",
      "registryIdentifier" : "MIR:00000378",
      "uris" : [ "urn:miriam:gxa.gene", "http://identifiers.org/gxa.gene/", "http://identifiers.org/gxa.gene", "https://identifiers.org/gxa.gene/", "https://identifiers.org/gxa.gene" ]
    },
    "HAMAP" : {
      "commonName" : "HAMAP",
      "homepage" : "https://hamap.expasy.org/",
      "registryIdentifier" : "MIR:00000292",
      "uris" : [ "urn:miriam:hamap", "http://identifiers.org/hamap/", "http://identifiers.org/hamap", "https://identifiers.org/hamap/", "https://identifiers.org/hamap" ]
    },
    "HCVDB" : {
      "commonName" : "HCVDB",
      "homepage" : "http://euhcvdb.ibcp.fr/euHCVdb/",
      "registryIdentifier" : "MIR:00000207",
      "uris" : [ "urn:miriam:hcvdb", "http://identifiers.org/hcvdb/", "http://identifiers.org/hcvdb", "https://identifiers.org/hcvdb/", "https://identifiers.org/hcvdb" ]
    },
    "HGMD" : {
      "commonName" : "HGMD",
      "homepage" : "http://www.hgmd.cf.ac.uk/ac/index.php",
      "registryIdentifier" : "MIR:00000392",
      "uris" : [ "urn:miriam:hgmd", "http://identifiers.org/hgmd/", "http://identifiers.org/hgmd", "https://identifiers.org/hgmd/", "https://identifiers.org/hgmd" ]
    },
    "HGNC" : {
      "commonName" : "HGNC",
      "homepage" : "http://www.genenames.org",
      "registryIdentifier" : "MIR:00000080",
      "uris" : [ "urn:miriam:hgnc", "http://identifiers.org/hgnc/", "http://identifiers.org/hgnc", "https://identifiers.org/hgnc/", "https://identifiers.org/hgnc" ]
    },
    "HGNC_FAMILY" : {
      "commonName" : "HGNC Family",
      "homepage" : "https://www.genenames.org/",
      "registryIdentifier" : "MIR:00000520",
      "uris" : [ "urn:miriam:hgnc.family", "http://identifiers.org/hgnc.family/", "http://identifiers.org/hgnc.family", "https://identifiers.org/hgnc.family/", "https://identifiers.org/hgnc.family" ]
    },
    "HGNC_SYMBOL" : {
      "commonName" : "HGNC Symbol",
      "homepage" : "http://www.genenames.org",
      "registryIdentifier" : "MIR:00000362",
      "uris" : [ "urn:miriam:hgnc.symbol", "http://identifiers.org/hgnc.symbol/", "http://identifiers.org/hgnc.symbol", "https://identifiers.org/hgnc.symbol/", "https://identifiers.org/hgnc.symbol" ]
    },
    "HMDB" : {
      "commonName" : "HMDB",
      "homepage" : "http://www.hmdb.ca/",
      "registryIdentifier" : "MIR:00000051",
      "uris" : [ "urn:miriam:hmdb", "http://identifiers.org/hmdb/", "http://identifiers.org/hmdb", "https://identifiers.org/hmdb/", "https://identifiers.org/hmdb" ]
    },
    "HOGENOM" : {
      "commonName" : "HOGENOM",
      "homepage" : "http://pbil.univ-lyon1.fr/databases/hogenom/",
      "registryIdentifier" : "MIR:00000213",
      "uris" : [ "urn:miriam:hogenom", "http://identifiers.org/hogenom/", "http://identifiers.org/hogenom", "https://identifiers.org/hogenom/", "https://identifiers.org/hogenom" ]
    },
    "HOMD_SEQUENCE_METAINFORMATION" : {
      "commonName" : "HOMD Sequence Metainformation",
      "homepage" : "http://www.homd.org/index.php",
      "registryIdentifier" : "MIR:00000170",
      "uris" : [ "urn:miriam:homd.seq", "http://identifiers.org/homd.seq/", "http://identifiers.org/homd.seq", "https://identifiers.org/homd.seq/", "https://identifiers.org/homd.seq" ]
    },
    "HOMD_TAXONOMY" : {
      "commonName" : "HOMD Taxonomy",
      "homepage" : "http://www.homd.org/index.php",
      "registryIdentifier" : "MIR:00000171",
      "uris" : [ "urn:miriam:homd.taxon", "http://identifiers.org/homd.taxon/", "http://identifiers.org/homd.taxon", "https://identifiers.org/homd.taxon/", "https://identifiers.org/homd.taxon" ]
    },
    "HOMEODOMAIN_RESEARCH" : {
      "commonName" : "Homeodomain Research",
      "homepage" : "http://research.nhgri.nih.gov/apps/homeodomain/web/",
      "registryIdentifier" : "MIR:00000497",
      "uris" : [ "urn:miriam:hdr", "http://identifiers.org/hdr/", "http://identifiers.org/hdr", "https://identifiers.org/hdr/", "https://identifiers.org/hdr" ]
    },
    "HOMOLOGENE" : {
      "commonName" : "HomoloGene",
      "homepage" : "https://www.ncbi.nlm.nih.gov/homologene/",
      "registryIdentifier" : "MIR:00000275",
      "uris" : [ "urn:miriam:homologene", "http://identifiers.org/homologene/", "http://identifiers.org/homologene", "https://identifiers.org/homologene/", "https://identifiers.org/homologene" ]
    },
    "HOVERGEN" : {
      "commonName" : "HOVERGEN",
      "homepage" : "http://pbil.univ-lyon1.fr/databases/hovergen.php",
      "registryIdentifier" : "MIR:00000074",
      "uris" : [ "urn:miriam:hovergen", "http://identifiers.org/hovergen/", "http://identifiers.org/hovergen", "https://identifiers.org/hovergen/", "https://identifiers.org/hovergen" ]
    },
    "HPA" : {
      "commonName" : "HPA",
      "homepage" : "http://www.proteinatlas.org/",
      "registryIdentifier" : "MIR:00000336",
      "uris" : [ "urn:miriam:hpa", "http://identifiers.org/hpa/", "http://identifiers.org/hpa", "https://identifiers.org/hpa/", "https://identifiers.org/hpa" ]
    },
    "HPRD" : {
      "commonName" : "HPRD",
      "homepage" : "http://www.hprd.org/",
      "registryIdentifier" : "MIR:00000377",
      "uris" : [ "urn:miriam:hprd", "http://identifiers.org/hprd/", "http://identifiers.org/hprd", "https://identifiers.org/hprd/", "https://identifiers.org/hprd" ]
    },
    "HSSP" : {
      "commonName" : "HSSP",
      "homepage" : "http://swift.cmbi.kun.nl/swift/hssp/",
      "registryIdentifier" : "MIR:00000215",
      "uris" : [ "urn:miriam:hssp", "http://identifiers.org/hssp/", "http://identifiers.org/hssp", "https://identifiers.org/hssp/", "https://identifiers.org/hssp" ]
    },
    "HUGE" : {
      "commonName" : "HUGE",
      "homepage" : "http://www.kazusa.or.jp/huge/",
      "registryIdentifier" : "MIR:00000263",
      "uris" : [ "urn:miriam:huge", "http://identifiers.org/huge/", "http://identifiers.org/huge", "https://identifiers.org/huge/", "https://identifiers.org/huge" ]
    },
    "HUMAN_DISEASE_ONTOLOGY" : {
      "commonName" : "Human Disease Ontology",
      "homepage" : "http://bioportal.bioontology.org/ontologies/DOID",
      "registryIdentifier" : "MIR:00000233",
      "uris" : [ "urn:miriam:obo.do", "urn:miriam:doid", "http://identifiers.org/doid/", "http://identifiers.org/DOID", "https://identifiers.org/doid/", "https://identifiers.org/DOID" ]
    },
    "HUMAN_PHENOTYPE_ONTOLOGY" : {
      "commonName" : "Human Phenotype Ontology",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/hp",
      "registryIdentifier" : "MIR:00000571",
      "uris" : [ "http://identifiers.org/hp/", "http://identifiers.org/HP", "https://identifiers.org/hp/", "https://identifiers.org/HP" ]
    },
    "HUMAN_PROTEOME_MAP_PEPTIDE" : {
      "commonName" : "Human Proteome Map Peptide",
      "homepage" : "http://www.humanproteomemap.org/index.php",
      "registryIdentifier" : "MIR:00000527",
      "uris" : [ "urn:miriam:hpm.peptide", "http://identifiers.org/hpm.peptide/", "http://identifiers.org/hpm.peptide", "https://identifiers.org/hpm.peptide/", "https://identifiers.org/hpm.peptide" ]
    },
    "HUMAN_PROTEOME_MAP_PROTEIN" : {
      "commonName" : "Human Proteome Map Protein",
      "homepage" : "http://www.humanproteomemap.org/index.php",
      "registryIdentifier" : "MIR:00000526",
      "uris" : [ "urn:miriam:hpm.protein", "http://identifiers.org/hpm.protein/", "http://identifiers.org/hpm.protein", "https://identifiers.org/hpm.protein/", "https://identifiers.org/hpm.protein" ]
    },
    "H_INVDB_LOCUS" : {
      "commonName" : "H-InvDb Locus",
      "homepage" : "http://h-invitational.jp/hinv/ahg-db/index.jsp",
      "registryIdentifier" : "MIR:00000167",
      "uris" : [ "urn:miriam:hinv.locus", "http://identifiers.org/hinv.locus/", "http://identifiers.org/hinv.locus", "https://identifiers.org/hinv.locus/", "https://identifiers.org/hinv.locus" ]
    },
    "H_INVDB_PROTEIN" : {
      "commonName" : "H-InvDb Protein",
      "homepage" : "http://h-invitational.jp/hinv/ahg-db/index.jsp",
      "registryIdentifier" : "MIR:00000169",
      "uris" : [ "urn:miriam:hinv.protein", "http://identifiers.org/hinv.protein/", "http://identifiers.org/hinv.protein", "https://identifiers.org/hinv.protein/", "https://identifiers.org/hinv.protein" ]
    },
    "H_INVDB_TRANSCRIPT" : {
      "commonName" : "H-InvDb Transcript",
      "homepage" : "http://h-invitational.jp/hinv/ahg-db/index.jsp",
      "registryIdentifier" : "MIR:00000168",
      "uris" : [ "urn:miriam:hinv.transcript", "http://identifiers.org/hinv.transcript/", "http://identifiers.org/hinv.transcript", "https://identifiers.org/hinv.transcript/", "https://identifiers.org/hinv.transcript" ]
    },
    "ICD" : {
      "commonName" : "ICD",
      "homepage" : "http://www.who.int/classifications/icd/en/",
      "registryIdentifier" : "MIR:00000009",
      "uris" : [ "urn:miriam:icd", "http://identifiers.org/icd/", "http://identifiers.org/icd", "https://identifiers.org/icd/", "https://identifiers.org/icd" ]
    },
    "ICEBERG_ELEMENT" : {
      "commonName" : "ICEberg element",
      "homepage" : "http://db-mml.sjtu.edu.cn/ICEberg/",
      "registryIdentifier" : "MIR:00000469",
      "uris" : [ "urn:miriam:iceberg.element", "http://identifiers.org/iceberg.element/", "http://identifiers.org/iceberg.element", "https://identifiers.org/iceberg.element/", "https://identifiers.org/iceberg.element" ]
    },
    "ICEBERG_FAMILY" : {
      "commonName" : "ICEberg family",
      "homepage" : "http://db-mml.sjtu.edu.cn/ICEberg/",
      "registryIdentifier" : "MIR:00000470",
      "uris" : [ "urn:miriam:iceberg.family", "http://identifiers.org/iceberg.family/", "http://identifiers.org/iceberg.family", "https://identifiers.org/iceberg.family/", "https://identifiers.org/iceberg.family" ]
    },
    "IDEAL" : {
      "commonName" : "IDEAL",
      "homepage" : "http://www.ideal.force.cs.is.nagoya-u.ac.jp/IDEAL/",
      "registryIdentifier" : "MIR:00000398",
      "uris" : [ "urn:miriam:ideal", "http://identifiers.org/ideal/", "http://identifiers.org/ideal", "https://identifiers.org/ideal/", "https://identifiers.org/ideal" ]
    },
    "IDENTIFIERS_ORG_TERMS" : {
      "commonName" : "Identifiers.org Terms",
      "homepage" : "https://identifiers.org/",
      "registryIdentifier" : "MIR:00000519",
      "uris" : [ "urn:miriam:idot", "http://identifiers.org/idot/", "http://identifiers.org/idot", "https://identifiers.org/idot/", "https://identifiers.org/idot" ]
    },
    "IMEX" : {
      "commonName" : "IMEx",
      "homepage" : "https://www.imexconsortium.org/",
      "registryIdentifier" : "MIR:00000122",
      "uris" : [ "urn:miriam:imex", "http://identifiers.org/imex/", "http://identifiers.org/imex", "https://identifiers.org/imex/", "https://identifiers.org/imex" ]
    },
    "IMGT_HLA" : {
      "commonName" : "IMGT HLA",
      "homepage" : "https://www.ebi.ac.uk/imgt/hla/allele.html",
      "registryIdentifier" : "MIR:00000331",
      "uris" : [ "urn:miriam:imgt.hla", "http://identifiers.org/imgt.hla/", "http://identifiers.org/imgt.hla", "https://identifiers.org/imgt.hla/", "https://identifiers.org/imgt.hla" ]
    },
    "IMGT_LIGM" : {
      "commonName" : "IMGT LIGM",
      "homepage" : "http://genius.embnet.dkfz-heidelberg.de/",
      "registryIdentifier" : "MIR:00000287",
      "uris" : [ "urn:miriam:imgt.ligm", "http://identifiers.org/imgt.ligm/", "http://identifiers.org/imgt.ligm", "https://identifiers.org/imgt.ligm/", "https://identifiers.org/imgt.ligm" ]
    },
    "INCHI" : {
      "commonName" : "InChI",
      "homepage" : "http://www.chemspider.com/",
      "registryIdentifier" : "MIR:00000383",
      "uris" : [ "urn:miriam:inchi", "http://identifiers.org/inchi/", "http://identifiers.org/inchi", "https://identifiers.org/inchi/", "https://identifiers.org/inchi" ]
    },
    "INCHIKEY" : {
      "commonName" : "InChIKey",
      "homepage" : "http://www.chemspider.com/",
      "registryIdentifier" : "MIR:00000387",
      "uris" : [ "urn:miriam:inchikey", "http://identifiers.org/inchikey/", "http://identifiers.org/inchi_key/", "http://identifiers.org/inchikey", "https://identifiers.org/inchikey/", "https://identifiers.org/inchi_key/", "https://identifiers.org/inchikey" ]
    },
    "INTACT" : {
      "commonName" : "IntAct",
      "homepage" : "https://www.ebi.ac.uk/intact/",
      "registryIdentifier" : "MIR:00000010",
      "uris" : [ "urn:miriam:intact", "http://identifiers.org/intact/", "http://identifiers.org/intact", "https://identifiers.org/intact/", "https://identifiers.org/intact" ]
    },
    "INTACT_MOLECULE" : {
      "commonName" : "IntAct Molecule",
      "homepage" : "https://www.ebi.ac.uk/intact/",
      "registryIdentifier" : "MIR:00000427",
      "uris" : [ "urn:miriam:intact.molecule", "http://identifiers.org/intact.molecule/", "http://identifiers.org/intact.molecule", "https://identifiers.org/intact.molecule/", "https://identifiers.org/intact.molecule" ]
    },
    "INTEGRATED_MICROBIAL_GENOMES_GENE" : {
      "commonName" : "Integrated Microbial Genomes Gene",
      "homepage" : "http://img.jgi.doe.gov/",
      "registryIdentifier" : "MIR:00000176",
      "uris" : [ "urn:miriam:img.gene", "http://identifiers.org/img.gene/", "http://identifiers.org/img.gene", "https://identifiers.org/img.gene/", "https://identifiers.org/img.gene" ]
    },
    "INTEGRATED_MICROBIAL_GENOMES_TAXON" : {
      "commonName" : "Integrated Microbial Genomes Taxon",
      "homepage" : "http://img.jgi.doe.gov/",
      "registryIdentifier" : "MIR:00000175",
      "uris" : [ "urn:miriam:img.taxon", "http://identifiers.org/img.taxon/", "http://identifiers.org/img.taxon", "https://identifiers.org/img.taxon/", "https://identifiers.org/img.taxon" ]
    },
    "INTERPRO" : {
      "commonName" : "InterPro",
      "homepage" : "http://www.ebi.ac.uk/interpro/",
      "registryIdentifier" : "MIR:00000011",
      "uris" : [ "urn:miriam:interpro", "http://identifiers.org/interpro/", "http://identifiers.org/interpro", "https://identifiers.org/interpro/", "https://identifiers.org/interpro" ]
    },
    "IRD_SEGMENT_SEQUENCE" : {
      "commonName" : "IRD Segment Sequence",
      "homepage" : "http://www.fludb.org/",
      "registryIdentifier" : "MIR:00000172",
      "uris" : [ "urn:miriam:ird.segment", "http://identifiers.org/ird.segment/", "http://identifiers.org/ird.segment", "https://identifiers.org/ird.segment/", "https://identifiers.org/ird.segment" ]
    },
    "IREFWEB" : {
      "commonName" : "iRefWeb",
      "homepage" : "http://wodaklab.org/iRefWeb/",
      "registryIdentifier" : "MIR:00000123",
      "uris" : [ "urn:miriam:irefweb", "http://identifiers.org/irefweb/", "http://identifiers.org/irefweb", "https://identifiers.org/irefweb/", "https://identifiers.org/irefweb" ]
    },
    "ISBN" : {
      "commonName" : "ISBN",
      "homepage" : "http://isbndb.com/",
      "registryIdentifier" : "MIR:00000064",
      "uris" : [ "urn:miriam:isbn", "http://identifiers.org/isbn/", "http://identifiers.org/isbn", "https://identifiers.org/isbn/", "https://identifiers.org/isbn" ]
    },
    "ISFINDER" : {
      "commonName" : "ISFinder",
      "homepage" : "http://www-is.biotoul.fr/i",
      "registryIdentifier" : "MIR:00000173",
      "uris" : [ "urn:miriam:isfinder", "http://identifiers.org/isfinder/", "http://identifiers.org/isfinder", "https://identifiers.org/isfinder/", "https://identifiers.org/isfinder" ]
    },
    "ISSN" : {
      "commonName" : "ISSN",
      "homepage" : "http://catalog.loc.gov/webvoy.htm",
      "registryIdentifier" : "MIR:00000301",
      "uris" : [ "urn:miriam:issn", "http://identifiers.org/issn/", "http://identifiers.org/issn", "https://identifiers.org/issn/", "https://identifiers.org/issn" ]
    },
    "IUPHAR_FAMILY" : {
      "commonName" : "IUPHAR family",
      "homepage" : "http://www.guidetopharmacology.org/",
      "registryIdentifier" : "MIR:00000317",
      "uris" : [ "urn:miriam:iuphar.family", "http://identifiers.org/iuphar.family/", "http://identifiers.org/iuphar.family", "https://identifiers.org/iuphar.family/", "https://identifiers.org/iuphar.family" ]
    },
    "IUPHAR_LIGAND" : {
      "commonName" : "IUPHAR ligand",
      "homepage" : "https://www.guidetopharmacology.org/GRAC/LigandListForward?database=all",
      "registryIdentifier" : "MIR:00000457",
      "uris" : [ "urn:miriam:iuphar.ligand", "http://identifiers.org/iuphar.ligand/", "http://identifiers.org/iuphar.ligand", "https://identifiers.org/iuphar.ligand/", "https://identifiers.org/iuphar.ligand" ]
    },
    "IUPHAR_RECEPTOR" : {
      "commonName" : "IUPHAR receptor",
      "homepage" : "http://www.guidetopharmacology.org/targets.jsp",
      "registryIdentifier" : "MIR:00000281",
      "uris" : [ "urn:miriam:iuphar.receptor", "http://identifiers.org/iuphar.receptor/", "http://identifiers.org/iuphar.receptor", "https://identifiers.org/iuphar.receptor/", "https://identifiers.org/iuphar.receptor" ]
    },
    "JAPAN_CHEMICAL_SUBSTANCE_DICTIONARY" : {
      "commonName" : "Japan Chemical Substance Dictionary",
      "homepage" : "http://jglobal.jst.go.jp/en/",
      "registryIdentifier" : "MIR:00000241",
      "uris" : [ "urn:miriam:jcsd", "http://identifiers.org/jcsd/", "http://identifiers.org/jcsd", "https://identifiers.org/jcsd/", "https://identifiers.org/jcsd" ]
    },
    "JAPAN_COLLECTION_OF_MICROORGANISMS" : {
      "commonName" : "Japan Collection of Microorganisms",
      "homepage" : "http://www.jcm.riken.go.jp/",
      "registryIdentifier" : "MIR:00000174",
      "uris" : [ "urn:miriam:jcm", "http://identifiers.org/jcm/", "http://identifiers.org/jcm", "https://identifiers.org/jcm/", "https://identifiers.org/jcm" ]
    },
    "JAX_MICE" : {
      "commonName" : "JAX Mice",
      "homepage" : "http://jaxmice.jax.org/",
      "registryIdentifier" : "MIR:00000337",
      "uris" : [ "urn:miriam:jaxmice", "http://identifiers.org/jaxmice/", "http://identifiers.org/jaxmice", "https://identifiers.org/jaxmice/", "https://identifiers.org/jaxmice" ]
    },
    "JCGGDB" : {
      "commonName" : "JCGGDB",
      "homepage" : "http://jcggdb.jp/index_en.html",
      "registryIdentifier" : "MIR:00000479",
      "uris" : [ "urn:miriam:jcggdb", "http://identifiers.org/jcggdb/", "http://identifiers.org/jcggdb", "https://identifiers.org/jcggdb/", "https://identifiers.org/jcggdb" ]
    },
    "JSTOR" : {
      "commonName" : "JSTOR",
      "homepage" : "http://www.jstor.org/",
      "registryIdentifier" : "MIR:00000444",
      "uris" : [ "urn:miriam:jstor", "http://identifiers.org/jstor/", "http://identifiers.org/jstor", "https://identifiers.org/jstor/", "https://identifiers.org/jstor" ]
    },
    "JWS_ONLINE" : {
      "commonName" : "JWS Online",
      "homepage" : "http://jjj.biochem.sun.ac.za/models/",
      "registryIdentifier" : "MIR:00000130",
      "uris" : [ "urn:miriam:jws", "http://identifiers.org/jws/", "http://identifiers.org/jws", "https://identifiers.org/jws/", "https://identifiers.org/jws" ]
    },
    "KEGG_COMPOUND" : {
      "commonName" : "Kegg Compound",
      "homepage" : "http://www.genome.jp/kegg/ligand.html",
      "registryIdentifier" : "MIR:00000013",
      "uris" : [ "urn:miriam:kegg.compound", "http://identifiers.org/kegg.compound/", "http://identifiers.org/kegg.compound", "https://identifiers.org/kegg.compound/", "https://identifiers.org/kegg.compound" ]
    },
    "KEGG_DISEASE" : {
      "commonName" : "KEGG Disease",
      "homepage" : "http://www.genome.jp/kegg/disease/",
      "registryIdentifier" : "MIR:00000475",
      "uris" : [ "urn:miriam:kegg.disease", "http://identifiers.org/kegg.disease/", "http://identifiers.org/kegg.disease", "https://identifiers.org/kegg.disease/", "https://identifiers.org/kegg.disease" ]
    },
    "KEGG_DRUG" : {
      "commonName" : "KEGG Drug",
      "homepage" : "https://www.genome.jp/kegg/drug/",
      "registryIdentifier" : "MIR:00000025",
      "uris" : [ "urn:miriam:kegg.drug", "http://identifiers.org/kegg.drug/", "http://identifiers.org/kegg.drug", "https://identifiers.org/kegg.drug/", "https://identifiers.org/kegg.drug" ]
    },
    "KEGG_ENVIRON" : {
      "commonName" : "KEGG Environ",
      "homepage" : "http://www.genome.jp/kegg/drug/environ.html",
      "registryIdentifier" : "MIR:00000389",
      "uris" : [ "urn:miriam:kegg.environ", "http://identifiers.org/kegg.environ/", "http://identifiers.org/kegg.environ", "https://identifiers.org/kegg.environ/", "https://identifiers.org/kegg.environ" ]
    },
    "KEGG_GENES" : {
      "commonName" : "Kegg Genes",
      "homepage" : "http://www.genome.jp/kegg/genes.html",
      "registryIdentifier" : "MIR:00000070",
      "uris" : [ "urn:miriam:kegg.genes", "http://identifiers.org/kegg.genes/", "http://identifiers.org/kegg.genes", "https://identifiers.org/kegg.genes/", "https://identifiers.org/kegg.genes" ]
    },
    "KEGG_GENOME" : {
      "commonName" : "KEGG Genome",
      "homepage" : "http://www.genome.jp/kegg/catalog/org_list.html",
      "registryIdentifier" : "MIR:00000238",
      "uris" : [ "urn:miriam:kegg.genome", "http://identifiers.org/kegg.genome/", "http://identifiers.org/kegg.genome", "https://identifiers.org/kegg.genome/", "https://identifiers.org/kegg.genome" ]
    },
    "KEGG_GLYCAN" : {
      "commonName" : "Kegg Glycan",
      "homepage" : "https://www.genome.jp/kegg/glycan/",
      "registryIdentifier" : "MIR:00000026",
      "uris" : [ "urn:miriam:kegg.glycan", "http://identifiers.org/kegg.glycan/", "http://identifiers.org/kegg.glycan", "https://identifiers.org/kegg.glycan/", "https://identifiers.org/kegg.glycan" ]
    },
    "KEGG_METAGENOME" : {
      "commonName" : "KEGG Metagenome",
      "homepage" : "http://www.genome.jp/kegg/catalog/org_list3.html",
      "registryIdentifier" : "MIR:00000239",
      "uris" : [ "urn:miriam:kegg.metagenome", "http://identifiers.org/kegg.metagenome/", "http://identifiers.org/kegg.metagenome", "https://identifiers.org/kegg.metagenome/", "https://identifiers.org/kegg.metagenome" ]
    },
    "KEGG_MODULE" : {
      "commonName" : "KEGG Module",
      "homepage" : "http://www.kegg.jp/kegg/module.html",
      "registryIdentifier" : "MIR:00000474",
      "uris" : [ "urn:miriam:kegg.module", "http://identifiers.org/kegg.module/", "http://identifiers.org/kegg.module", "https://identifiers.org/kegg.module/", "https://identifiers.org/kegg.module" ]
    },
    "KEGG_ORTHOLOGY" : {
      "commonName" : "KEGG Orthology",
      "homepage" : "http://www.genome.jp/kegg/ko.html",
      "registryIdentifier" : "MIR:00000116",
      "uris" : [ "urn:miriam:kegg.orthology", "http://identifiers.org/kegg.orthology/", "http://identifiers.org/kegg.orthology", "https://identifiers.org/kegg.orthology/", "https://identifiers.org/kegg.orthology" ]
    },
    "KEGG_PATHWAY" : {
      "commonName" : "Kegg Pathway",
      "homepage" : "http://www.genome.jp/kegg/pathway.html",
      "registryIdentifier" : "MIR:00000012",
      "uris" : [ "urn:miriam:kegg.pathway", "http://identifiers.org/kegg.pathway/", "http://identifiers.org/kegg.pathway", "https://identifiers.org/kegg.pathway/", "https://identifiers.org/kegg.pathway" ]
    },
    "KEGG_REACTION" : {
      "commonName" : "Kegg Reaction",
      "homepage" : "http://www.genome.jp/kegg/reaction/",
      "registryIdentifier" : "MIR:00000014",
      "uris" : [ "urn:miriam:kegg.reaction", "http://identifiers.org/kegg.reaction/", "http://identifiers.org/kegg.reaction", "https://identifiers.org/kegg.reaction/", "https://identifiers.org/kegg.reaction" ]
    },
    "KISAO" : {
      "commonName" : "KiSAO",
      "homepage" : "http://bioportal.bioontology.org/ontologies/KISAO",
      "registryIdentifier" : "MIR:00000108",
      "uris" : [ "urn:miriam:biomodels.kisao", "http://identifiers.org/biomodels.kisao/", "http://identifiers.org/biomodels.kisao", "https://identifiers.org/biomodels.kisao/", "https://identifiers.org/biomodels.kisao" ]
    },
    "KNAPSACK" : {
      "commonName" : "KnapSack",
      "homepage" : "http://kanaya.aist-nara.ac.jp/KNApSAcK/",
      "registryIdentifier" : "MIR:00000271",
      "uris" : [ "urn:miriam:knapsack", "http://identifiers.org/knapsack/", "http://identifiers.org/knapsack", "https://identifiers.org/knapsack/", "https://identifiers.org/knapsack" ]
    },
    "LIGANDBOX" : {
      "commonName" : "LigandBox",
      "homepage" : "http://www.mypresto5.com/ligandbox/cgi-bin/index.cgi?LANG=en",
      "registryIdentifier" : "MIR:00000477",
      "uris" : [ "urn:miriam:ligandbox", "http://identifiers.org/ligandbox/", "http://identifiers.org/ligandbox", "https://identifiers.org/ligandbox/", "https://identifiers.org/ligandbox" ]
    },
    "LIGAND_EXPO" : {
      "commonName" : "Ligand Expo",
      "homepage" : "http://ligand-depot.rutgers.edu/index.html",
      "registryIdentifier" : "MIR:00000062",
      "uris" : [ "urn:miriam:ligandexpo", "http://identifiers.org/ligandexpo/", "http://identifiers.org/ligandexpo", "https://identifiers.org/ligandexpo/", "https://identifiers.org/ligandexpo" ]
    },
    "LIGAND_GATED_ION_CHANNEL_DATABASE" : {
      "commonName" : "Ligand-Gated Ion Channel database",
      "homepage" : "https://www.ebi.ac.uk/compneur-srv/LGICdb/LGICdb.php",
      "registryIdentifier" : "MIR:00000087",
      "uris" : [ "urn:miriam:lgic", "http://identifiers.org/lgic/", "http://identifiers.org/lgic", "https://identifiers.org/lgic/", "https://identifiers.org/lgic" ]
    },
    "LINCS_CELL" : {
      "commonName" : "LINCS Cell",
      "homepage" : "http://lincsportal.ccs.miami.edu/cells/",
      "registryIdentifier" : "MIR:00000544",
      "uris" : [ "urn:miriam:lincs.cell", "http://identifiers.org/lincs.cell/", "http://identifiers.org/lincs.cell", "https://identifiers.org/lincs.cell/", "https://identifiers.org/lincs.cell" ]
    },
    "LINCS_PROTEIN" : {
      "commonName" : "LINCS Protein",
      "homepage" : "http://lincs.hms.harvard.edu/db/proteins/",
      "registryIdentifier" : "MIR:00000545",
      "uris" : [ "urn:miriam:lincs.protein", "http://identifiers.org/lincs.protein/", "http://identifiers.org/lincs.protein", "https://identifiers.org/lincs.protein/", "https://identifiers.org/lincs.protein" ]
    },
    "LIPID_BANK" : {
      "commonName" : "LipidBank",
      "homepage" : "http://lipidbank.jp/index.html",
      "registryIdentifier" : "MIR:00000115",
      "uris" : [ "urn:miriam:lipidbank", "http://identifiers.org/lipidbank/", "http://identifiers.org/lipidbank", "https://identifiers.org/lipidbank/", "https://identifiers.org/lipidbank" ]
    },
    "LIPID_MAPS" : {
      "commonName" : "LIPID MAPS",
      "homepage" : "http://www.lipidmaps.org",
      "registryIdentifier" : "MIR:00000052",
      "uris" : [ "urn:miriam:lipidmaps", "http://identifiers.org/lipidmaps/", "http://identifiers.org/lipidmaps", "https://identifiers.org/lipidmaps/", "https://identifiers.org/lipidmaps" ]
    },
    "LOCUS_REFERENCE_GENOMIC" : {
      "commonName" : "Locus Reference Genomic",
      "homepage" : "http://www.ensembl.org/",
      "registryIdentifier" : "MIR:00000376",
      "uris" : [ "urn:miriam:lrg", "http://identifiers.org/lrg/", "http://identifiers.org/lrg", "https://identifiers.org/lrg/", "https://identifiers.org/lrg" ]
    },
    "MACIE" : {
      "commonName" : "MACiE",
      "homepage" : "https://www.ebi.ac.uk/thornton-srv/databases/MACiE/index.html",
      "registryIdentifier" : "MIR:00000077",
      "uris" : [ "urn:miriam:macie", "http://identifiers.org/macie/", "http://identifiers.org/macie", "https://identifiers.org/macie/", "https://identifiers.org/macie" ]
    },
    "MAIZEGDB_LOCUS" : {
      "commonName" : "MaizeGDB Locus",
      "homepage" : "http://www.maizegdb.org/",
      "registryIdentifier" : "MIR:00000177",
      "uris" : [ "urn:miriam:maizegdb.locus", "http://identifiers.org/maizegdb.locus/", "http://identifiers.org/maizegdb.locus", "https://identifiers.org/maizegdb.locus/", "https://identifiers.org/maizegdb.locus" ]
    },
    "MASSBANK" : {
      "commonName" : "MassBank",
      "homepage" : "http://www.massbank.jp",
      "registryIdentifier" : "MIR:00000273",
      "uris" : [ "urn:miriam:massbank", "http://identifiers.org/massbank/", "http://identifiers.org/massbank", "https://identifiers.org/massbank/", "https://identifiers.org/massbank" ]
    },
    "MATHEMATICAL_MODELLING_ONTOLOGY" : {
      "commonName" : "Mathematical Modelling Ontology",
      "homepage" : "http://bioportal.bioontology.org/ontologies/MAMO",
      "registryIdentifier" : "MIR:00000517",
      "uris" : [ "urn:miriam:mamo", "http://identifiers.org/mamo/", "http://identifiers.org/mamo", "https://identifiers.org/mamo/", "https://identifiers.org/mamo" ]
    },
    "MATRIXDB" : {
      "commonName" : "MatrixDB",
      "homepage" : "http://matrixdb.univ-lyon1.fr/",
      "registryIdentifier" : "MIR:00000068",
      "uris" : [ "urn:miriam:matrixdb.association", "http://identifiers.org/matrixdb.association/", "http://identifiers.org/matrixdb.association", "https://identifiers.org/matrixdb.association/", "https://identifiers.org/matrixdb.association" ]
    },
    "MEDLINEPLUS" : {
      "commonName" : "MedlinePlus",
      "homepage" : "http://www.nlm.nih.gov/medlineplus/",
      "registryIdentifier" : "MIR:00000476",
      "uris" : [ "urn:miriam:medlineplus", "http://identifiers.org/medlineplus/", "http://identifiers.org/medlineplus", "https://identifiers.org/medlineplus/", "https://identifiers.org/medlineplus" ]
    },
    "MEROPS" : {
      "commonName" : "MEROPS",
      "homepage" : "http://merops.sanger.ac.uk/index.htm",
      "registryIdentifier" : "MIR:00000059",
      "uris" : [ "urn:miriam:merops", "http://identifiers.org/merops/", "http://identifiers.org/merops", "https://identifiers.org/merops/", "https://identifiers.org/merops" ]
    },
    "MEROPS_FAMILY" : {
      "commonName" : "MEROPS Family",
      "homepage" : "http://merops.sanger.ac.uk/index.htm",
      "registryIdentifier" : "MIR:00000302",
      "uris" : [ "urn:miriam:merops.family", "http://identifiers.org/merops.family/", "http://identifiers.org/merops.family", "https://identifiers.org/merops.family/", "https://identifiers.org/merops.family" ]
    },
    "MEROPS_INHIBITOR" : {
      "commonName" : "MEROPS Inhibitor",
      "homepage" : "http://merops.sanger.ac.uk/index.htm",
      "registryIdentifier" : "MIR:00000491",
      "uris" : [ "urn:miriam:merops.inhibitor", "http://identifiers.org/merops.inhibitor/", "http://identifiers.org/merops.inhibitor", "https://identifiers.org/merops.inhibitor/", "https://identifiers.org/merops.inhibitor" ]
    },
    "MESH_2012" : {
      "commonName" : "MeSH",
      "homepage" : "http://www.nlm.nih.gov/mesh/",
      "registryIdentifier" : "MIR:00000560",
      "uris" : [ "urn:miriam:mesh", "urn:miriam:mesh.2012", "urn:miriam:mesh.2013", "http://identifiers.org/mesh/", "http://identifiers.org/mesh", "https://identifiers.org/mesh/", "https://identifiers.org/mesh" ]
    },
    "METABOLIGHTS" : {
      "commonName" : "MetaboLights",
      "homepage" : "https://www.ebi.ac.uk/metabolights/",
      "registryIdentifier" : "MIR:00000380",
      "uris" : [ "urn:miriam:metabolights", "http://identifiers.org/metabolights/", "http://identifiers.org/metabolights", "https://identifiers.org/metabolights/", "https://identifiers.org/metabolights" ]
    },
    "METANETX_CHEMICAL" : {
      "commonName" : "MetaNetX chemical",
      "homepage" : "https://www.metanetx.org/",
      "registryIdentifier" : "MIR:00000567",
      "uris" : [ "http://identifiers.org/metanetx.chemical/", "http://identifiers.org/metanetx.chemical", "https://identifiers.org/metanetx.chemical/", "https://identifiers.org/metanetx.chemical" ]
    },
    "METANETX_COMPARTMENT" : {
      "commonName" : "MetaNetX compartment",
      "homepage" : "https://www.metanetx.org/",
      "registryIdentifier" : "MIR:00000569",
      "uris" : [ "http://identifiers.org/metanetx.compartment/", "http://identifiers.org/metanetx.compartment", "https://identifiers.org/metanetx.compartment/", "https://identifiers.org/metanetx.compartment" ]
    },
    "METANETX_REACTION" : {
      "commonName" : "MetaNetX reaction",
      "homepage" : "https://www.metanetx.org/",
      "registryIdentifier" : "MIR:00000568",
      "uris" : [ "http://identifiers.org/metanetx.reaction/", "http://identifiers.org/metanetx.reaction", "https://identifiers.org/metanetx.reaction/", "https://identifiers.org/metanetx.reaction" ]
    },
    "METLIN" : {
      "commonName" : "METLIN",
      "homepage" : "http://masspec.scripps.edu/",
      "registryIdentifier" : "MIR:00000322",
      "uris" : [ "urn:miriam:metlin", "http://identifiers.org/metlin/", "http://identifiers.org/metlin", "https://identifiers.org/metlin/", "https://identifiers.org/metlin" ]
    },
    "MGD" : {
      "commonName" : "Mouse Genome Database",
      "homepage" : "http://www.informatics.jax.org/",
      "registryIdentifier" : "MIR:00000037",
      "uris" : [ "urn:miriam:mgd", "http://identifiers.org/mgi/", "http://identifiers.org/MGI", "https://identifiers.org/mgi/", "https://identifiers.org/MGI" ]
    },
    "MGED_ONTOLOGY" : {
      "commonName" : "MGED Ontology",
      "homepage" : "http://bioportal.bioontology.org/",
      "registryIdentifier" : "MIR:00000303",
      "uris" : [ "urn:miriam:mo", "http://identifiers.org/mo/", "http://identifiers.org/mo", "https://identifiers.org/mo/", "https://identifiers.org/mo" ]
    },
    "MGNIFY_PROJECT" : {
      "commonName" : "MGnify Project",
      "homepage" : "https://www.ebi.ac.uk/metagenomics",
      "registryIdentifier" : "MIR:00000535",
      "uris" : [ "urn:miriam:ebimetagenomics.proj", "http://identifiers.org/mgnify.proj/", "http://identifiers.org/mgnify.proj", "https://identifiers.org/mgnify.proj/", "https://identifiers.org/mgnify.proj" ]
    },
    "MGNIFY_SAMPLE" : {
      "commonName" : "MGnify Sample",
      "homepage" : "https://www.ebi.ac.uk/metagenomics",
      "registryIdentifier" : "MIR:00000510",
      "uris" : [ "urn:miriam:ebimetagenomics.samp", "urn:miriam:ebimetagenomics", "http://identifiers.org/mgnify.samp/", "http://identifiers.org/mgnify.samp", "https://identifiers.org/mgnify.samp/", "https://identifiers.org/mgnify.samp" ]
    },
    "MI" : {
      "commonName" : "Molecular Interactions Ontology",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/mi",
      "registryIdentifier" : "MIR:00000109",
      "uris" : [ "urn:miriam:psimi", "urn:miriam:obo.mi", "http://identifiers.org/MI/", "http://identifiers.org/MI", "https://identifiers.org/MI/", "https://identifiers.org/MI" ]
    },
    "MICROBIAL_PROTEIN_INTERACTION_DATABASE" : {
      "commonName" : "Microbial Protein Interaction Database",
      "homepage" : "http://www.jcvi.org/mpidb/about.php",
      "registryIdentifier" : "MIR:00000124",
      "uris" : [ "urn:miriam:mpid", "http://identifiers.org/mpid/", "http://identifiers.org/mpid", "https://identifiers.org/mpid/", "https://identifiers.org/mpid" ]
    },
    "MICROSPORIDIADB" : {
      "commonName" : "MicrosporidiaDB",
      "homepage" : "http://microsporidiadb.org/micro/",
      "registryIdentifier" : "MIR:00000152",
      "uris" : [ "urn:miriam:microsporidia", "http://identifiers.org/microsporidia/", "http://identifiers.org/microsporidia", "https://identifiers.org/microsporidia/", "https://identifiers.org/microsporidia" ]
    },
    "MIMODB" : {
      "commonName" : "MimoDB",
      "homepage" : "http://immunet.cn/bdb/",
      "registryIdentifier" : "MIR:00000251",
      "uris" : [ "urn:miriam:mimodb", "http://identifiers.org/mimodb/", "http://identifiers.org/mimodb", "https://identifiers.org/mimodb/", "https://identifiers.org/mimodb" ]
    },
    "MINT" : {
      "commonName" : "MINT",
      "homepage" : "http://mint.bio.uniroma2.it/mint/",
      "registryIdentifier" : "MIR:00000042",
      "uris" : [ "urn:miriam:mint", "http://identifiers.org/mint/", "http://identifiers.org/mint", "https://identifiers.org/mint/", "https://identifiers.org/mint" ]
    },
    "MIPMODDB" : {
      "commonName" : "MIPModDB",
      "homepage" : "http://bioinfo.iitk.ac.in/MIPModDB",
      "registryIdentifier" : "MIR:00000256",
      "uris" : [ "urn:miriam:mipmod", "http://identifiers.org/mipmod/", "http://identifiers.org/mipmod", "https://identifiers.org/mipmod/", "https://identifiers.org/mipmod" ]
    },
    "MIREX" : {
      "commonName" : "mirEX",
      "homepage" : "http://comgen.pl/mirex/?page=home",
      "registryIdentifier" : "MIR:00000329",
      "uris" : [ "urn:miriam:mirex", "http://identifiers.org/mirex/", "http://identifiers.org/mirex", "https://identifiers.org/mirex/", "https://identifiers.org/mirex" ]
    },
    "MIRIAM_REGISTRY_COLLECTION" : {
      "commonName" : "MIRIAM Registry collection",
      "homepage" : "https://www.ebi.ac.uk/miriam/",
      "registryIdentifier" : "MIR:00000008",
      "uris" : [ "urn:miriam:miriam.collection", "urn:miriam:miriam", "urn:miriam:miriam.datatype", "http://identifiers.org/miriam.collection/", "http://identifiers.org/miriam.collection", "https://identifiers.org/miriam.collection/", "https://identifiers.org/miriam.collection" ]
    },
    "MIRIAM_REGISTRY_RESOURCE" : {
      "commonName" : "MIRIAM Registry resource",
      "homepage" : "https://www.ebi.ac.uk/miriam/",
      "registryIdentifier" : "MIR:00000188",
      "uris" : [ "urn:miriam:miriam.resource", "http://identifiers.org/miriam.resource/", "http://identifiers.org/miriam.resource", "https://identifiers.org/miriam.resource/", "https://identifiers.org/miriam.resource" ]
    },
    "MIRNEST" : {
      "commonName" : "miRNEST",
      "homepage" : "http://rhesus.amu.edu.pl/mirnest/copy/",
      "registryIdentifier" : "MIR:00000246",
      "uris" : [ "urn:miriam:mirnest", "http://identifiers.org/mirnest/", "http://identifiers.org/mirnest", "https://identifiers.org/mirnest/", "https://identifiers.org/mirnest" ]
    },
    "MIR_TAR_BASE_MATURE_SEQUENCE" : {
      "commonName" : "miRTarBase Mature Sequence Database",
      "homepage" : "http://mirtarbase.mbc.nctu.edu.tw/",
      "registryIdentifier" : "MIR:00000562",
      "uris" : [ "urn:miriam:mirtarbase", "http://identifiers.org/mirtarbase/", "http://identifiers.org/mirtarbase", "https://identifiers.org/mirtarbase/", "https://identifiers.org/mirtarbase" ]
    },
    "MI_R_BASE_MATURE_SEQUENCE" : {
      "commonName" : "miRBase Mature Sequence Database",
      "homepage" : "http://www.mirbase.org/",
      "registryIdentifier" : "MIR:00000235",
      "uris" : [ "urn:miriam:mirbase.mature", "http://identifiers.org/mirbase.mature/", "http://identifiers.org/mirbase.mature", "https://identifiers.org/mirbase.mature/", "https://identifiers.org/mirbase.mature" ]
    },
    "MI_R_BASE_SEQUENCE" : {
      "commonName" : "miRBase Sequence Database",
      "homepage" : "http://www.mirbase.org/",
      "registryIdentifier" : "MIR:00000078",
      "uris" : [ "urn:miriam:mirbase", "http://identifiers.org/mirbase/", "http://identifiers.org/mirbase", "https://identifiers.org/mirbase/", "https://identifiers.org/mirbase" ]
    },
    "MMRRC" : {
      "commonName" : "MMRRC",
      "homepage" : "http://www.mmrrc.org/",
      "registryIdentifier" : "MIR:00000324",
      "uris" : [ "urn:miriam:mmrrc", "http://identifiers.org/mmrrc/", "http://identifiers.org/mmrrc", "https://identifiers.org/mmrrc/", "https://identifiers.org/mmrrc" ]
    },
    "MOD" : {
      "commonName" : "Protein Modification Ontology",
      "homepage" : "https://bioportal.bioontology.org/ontologies/PSIMOD",
      "registryIdentifier" : "MIR:00000056",
      "uris" : [ "urn:miriam:obo.psi-mod", "urn:miriam:psimod", "urn:miriam:mod", "http://identifiers.org/mod/", "http://identifiers.org/psimod/", "http://identifiers.org/obo.psi-mod/", "http://identifiers.org/MOD", "https://identifiers.org/mod/", "https://identifiers.org/obo.psi-mod/", "https://identifiers.org/psimod/", "https://identifiers.org/MOD" ]
    },
    "MODELDB" : {
      "commonName" : "ModelDB",
      "homepage" : "http://senselab.med.yale.edu/ModelDB/",
      "registryIdentifier" : "MIR:00000131",
      "uris" : [ "urn:miriam:modeldb", "http://identifiers.org/modeldb/", "http://identifiers.org/modeldb", "https://identifiers.org/modeldb/", "https://identifiers.org/modeldb" ]
    },
    "MOLBASE" : {
      "commonName" : "Molbase",
      "homepage" : "http://www.molbase.com/",
      "registryIdentifier" : "MIR:00000458",
      "uris" : [ "urn:miriam:molbase", "http://identifiers.org/molbase/", "http://identifiers.org/molbase", "https://identifiers.org/molbase/", "https://identifiers.org/molbase" ]
    },
    "MOLECULAR_MODELING_DATABASE" : {
      "commonName" : "Molecular Modeling Database",
      "homepage" : "http://www.ncbi.nlm.nih.gov/sites/entrez?db=structure",
      "registryIdentifier" : "MIR:00000121",
      "uris" : [ "urn:miriam:mmdb", "http://identifiers.org/mmdb/", "http://identifiers.org/mmdb", "https://identifiers.org/mmdb/", "https://identifiers.org/mmdb" ]
    },
    "MOUSE_ADULT_GROSS_ANATOMY" : {
      "commonName" : "Mouse Adult Gross Anatomy",
      "homepage" : "http://bioportal.bioontology.org/ontologies/MA",
      "registryIdentifier" : "MIR:00000445",
      "uris" : [ "urn:miriam:ma", "http://identifiers.org/ma/", "http://identifiers.org/MA", "https://identifiers.org/ma/", "https://identifiers.org/MA" ]
    },
    "MYCOBANK" : {
      "commonName" : "MycoBank",
      "homepage" : "http://www.mycobank.org/",
      "registryIdentifier" : "MIR:00000178",
      "uris" : [ "urn:miriam:mycobank", "http://identifiers.org/mycobank/", "http://identifiers.org/mycobank", "https://identifiers.org/mycobank/", "https://identifiers.org/mycobank" ]
    },
    "MYCOBROWSER_LEPRAE" : {
      "commonName" : "MycoBrowser leprae",
      "homepage" : "http://mycobrowser.epfl.ch/leprosy.html",
      "registryIdentifier" : "MIR:00000217",
      "uris" : [ "urn:miriam:myco.lepra", "http://identifiers.org/myco.lepra/", "http://identifiers.org/myco.lepra", "https://identifiers.org/myco.lepra/", "https://identifiers.org/myco.lepra" ]
    },
    "MYCOBROWSER_MARINUM" : {
      "commonName" : "MycoBrowser marinum",
      "homepage" : "http://mycobrowser.epfl.ch/marinolist.html",
      "registryIdentifier" : "MIR:00000218",
      "uris" : [ "urn:miriam:myco.marinum", "http://identifiers.org/myco.marinum/", "http://identifiers.org/myco.marinum", "https://identifiers.org/myco.marinum/", "https://identifiers.org/myco.marinum" ]
    },
    "MYCOBROWSER_SMEGMATIS" : {
      "commonName" : "MycoBrowser smegmatis",
      "homepage" : "http://mycobrowser.epfl.ch/smegmalist.html",
      "registryIdentifier" : "MIR:00000219",
      "uris" : [ "urn:miriam:myco.smeg", "http://identifiers.org/myco.smeg/", "http://identifiers.org/myco.smeg", "https://identifiers.org/myco.smeg/", "https://identifiers.org/myco.smeg" ]
    },
    "MYCOBROWSER_TUBERCULOSIS" : {
      "commonName" : "MycoBrowser tuberculosis",
      "homepage" : "http://tuberculist.epfl.ch/",
      "registryIdentifier" : "MIR:00000216",
      "uris" : [ "urn:miriam:myco.tuber", "http://identifiers.org/myco.tuber/", "http://identifiers.org/myco.tuber", "https://identifiers.org/myco.tuber/", "https://identifiers.org/myco.tuber" ]
    },
    "NAPP" : {
      "commonName" : "NAPP",
      "homepage" : "http://napp.u-psud.fr/",
      "registryIdentifier" : "MIR:00000247",
      "uris" : [ "urn:miriam:napp", "http://identifiers.org/napp/", "http://identifiers.org/napp", "https://identifiers.org/napp/", "https://identifiers.org/napp" ]
    },
    "NARCIS" : {
      "commonName" : "NARCIS",
      "homepage" : "http://www.narcis.nl/?Language=en",
      "registryIdentifier" : "MIR:00000240",
      "uris" : [ "urn:miriam:narcis", "http://identifiers.org/narcis/", "http://identifiers.org/narcis", "https://identifiers.org/narcis/", "https://identifiers.org/narcis" ]
    },
    "NASC_CODE" : {
      "commonName" : "NASC code",
      "homepage" : "http://arabidopsis.info/",
      "registryIdentifier" : "MIR:00000304",
      "uris" : [ "urn:miriam:nasc", "http://identifiers.org/nasc/", "http://identifiers.org/nasc", "https://identifiers.org/nasc/", "https://identifiers.org/nasc" ]
    },
    "NATIONAL_BIBLIOGRAPHY_NUMBER" : {
      "commonName" : "National Bibliography Number",
      "homepage" : "http://nbn-resolving.org/resolve_urn.htm",
      "registryIdentifier" : "MIR:00000381",
      "uris" : [ "urn:miriam:nbn", "http://identifiers.org/nbn/", "http://identifiers.org/nbn", "https://identifiers.org/nbn/", "https://identifiers.org/nbn" ]
    },
    "NATIONAL_DRUG_CODE" : {
      "commonName" : "National Drug Code",
      "homepage" : "http://www.accessdata.fda.gov/scripts/cder/ndc/",
      "registryIdentifier" : "MIR:00000431",
      "uris" : [ "urn:miriam:ndc", "http://identifiers.org/ndc/", "http://identifiers.org/ndc", "https://identifiers.org/ndc/", "https://identifiers.org/ndc" ]
    },
    "NCBI_PROTEIN" : {
      "commonName" : "NCBI Protein",
      "homepage" : "https://www.ncbi.nlm.nih.gov/protein",
      "registryIdentifier" : "MIR:00000344",
      "uris" : [ "urn:miriam:ncbiprotein", "http://identifiers.org/ncbiprotein/", "http://identifiers.org/ncbiprotein", "https://identifiers.org/ncbiprotein/", "https://identifiers.org/ncbiprotein" ]
    },
    "NCIM" : {
      "commonName" : "NCIm",
      "homepage" : "http://ncim.nci.nih.gov/",
      "registryIdentifier" : "MIR:00000353",
      "uris" : [ "urn:miriam:ncim", "http://identifiers.org/ncim/", "http://identifiers.org/ncim", "https://identifiers.org/ncim/", "https://identifiers.org/ncim" ]
    },
    "NCIT" : {
      "commonName" : "NCIt",
      "homepage" : "http://ncit.nci.nih.gov/",
      "registryIdentifier" : "MIR:00000139",
      "uris" : [ "urn:miriam:ncit", "http://identifiers.org/ncit/", "http://identifiers.org/ncit", "https://identifiers.org/ncit/", "https://identifiers.org/ncit" ]
    },
    "NCI_PATHWAY_INTERACTION_DATABASE_PATHWAY" : {
      "commonName" : "NCI Pathway Interaction Database: Pathway",
      "homepage" : "http://pid.nci.nih.gov/",
      "registryIdentifier" : "MIR:00000133",
      "uris" : [ "urn:miriam:pid.pathway", "http://identifiers.org/pid.pathway/", "http://identifiers.org/pid.pathway", "https://identifiers.org/pid.pathway/", "https://identifiers.org/pid.pathway" ]
    },
    "NEUROLEX" : {
      "commonName" : "NeuroLex",
      "homepage" : "http://www.neurolex.org/wiki/Main_Page",
      "registryIdentifier" : "MIR:00000126",
      "uris" : [ "urn:miriam:neurolex", "http://identifiers.org/neurolex/", "http://identifiers.org/neurolex", "https://identifiers.org/neurolex/", "https://identifiers.org/neurolex" ]
    },
    "NEUROMORPHO" : {
      "commonName" : "NeuroMorpho",
      "homepage" : "http://neuromorpho.org/index.jsp",
      "registryIdentifier" : "MIR:00000095",
      "uris" : [ "urn:miriam:neuromorpho", "http://identifiers.org/neuromorpho/", "http://identifiers.org/neuromorpho", "https://identifiers.org/neuromorpho/", "https://identifiers.org/neuromorpho" ]
    },
    "NEURONDB" : {
      "commonName" : "NeuronDB",
      "homepage" : "http://senselab.med.yale.edu/NeuronDB/",
      "registryIdentifier" : "MIR:00000094",
      "uris" : [ "urn:miriam:neurondb", "http://identifiers.org/neurondb/", "http://identifiers.org/neurondb", "https://identifiers.org/neurondb/", "https://identifiers.org/neurondb" ]
    },
    "NEXTDB" : {
      "commonName" : "NEXTDB",
      "homepage" : "http://nematode.lab.nig.ac.jp/",
      "registryIdentifier" : "MIR:00000289",
      "uris" : [ "urn:miriam:nextdb", "http://identifiers.org/nextdb/", "http://identifiers.org/nextdb", "https://identifiers.org/nextdb/", "https://identifiers.org/nextdb" ]
    },
    "NEXTPROT" : {
      "commonName" : "nextProt",
      "homepage" : "https://www.nextprot.org/",
      "registryIdentifier" : "MIR:00000236",
      "uris" : [ "urn:miriam:nextprot", "http://identifiers.org/nextprot/", "http://identifiers.org/nextprot", "https://identifiers.org/nextprot/", "https://identifiers.org/nextprot" ]
    },
    "NIAEST" : {
      "commonName" : "NIAEST",
      "homepage" : "http://lgsun.grc.nia.nih.gov/cDNA/",
      "registryIdentifier" : "MIR:00000305",
      "uris" : [ "urn:miriam:niaest", "http://identifiers.org/niaest/", "http://identifiers.org/niaest", "https://identifiers.org/niaest/", "https://identifiers.org/niaest" ]
    },
    "NITE_BIOLOGICAL_RESEARCH_CENTER_CATALOGUE" : {
      "commonName" : "NITE Biological Research Center Catalogue",
      "homepage" : "http://www.nbrc.nite.go.jp/e/index.html",
      "registryIdentifier" : "MIR:00000179",
      "uris" : [ "urn:miriam:nbrc", "http://identifiers.org/nbrc/", "http://identifiers.org/nbrc", "https://identifiers.org/nbrc/", "https://identifiers.org/nbrc" ]
    },
    "NONCODE_V3" : {
      "commonName" : "NONCODE v3",
      "homepage" : "http://www.noncode.org/",
      "registryIdentifier" : "MIR:00000248",
      "uris" : [ "urn:miriam:noncodev3", "urn:miriam:noncode", "http://identifiers.org/noncodev3/", "http://identifiers.org/noncodev3", "https://identifiers.org/noncodev3/", "https://identifiers.org/noncodev3" ]
    },
    "NONCODE_V4_GENE" : {
      "commonName" : "NONCODE v4 Gene",
      "homepage" : "http://www.bioinfo.org/NONCODEv4/",
      "registryIdentifier" : "MIR:00000480",
      "uris" : [ "urn:miriam:noncodev4.gene", "http://identifiers.org/noncodev4.gene/", "http://identifiers.org/noncodev4.gene", "https://identifiers.org/noncodev4.gene/", "https://identifiers.org/noncodev4.gene" ]
    },
    "NONCODE_V4_TRANSCRIPT" : {
      "commonName" : "NONCODE v4 Transcript",
      "homepage" : "http://www.bioinfo.org/NONCODEv4/",
      "registryIdentifier" : "MIR:00000481",
      "uris" : [ "urn:miriam:noncodev4.rna", "http://identifiers.org/noncodev4.rna/", "http://identifiers.org/noncodev4.rna", "https://identifiers.org/noncodev4.rna/", "https://identifiers.org/noncodev4.rna" ]
    },
    "NORINE" : {
      "commonName" : "NORINE",
      "homepage" : "http://bioinfo.lifl.fr/norine/",
      "registryIdentifier" : "MIR:00000498",
      "uris" : [ "urn:miriam:norine", "http://identifiers.org/norine/", "http://identifiers.org/norine", "https://identifiers.org/norine/", "https://identifiers.org/norine" ]
    },
    "NUCLEARDB" : {
      "commonName" : "NucleaRDB",
      "homepage" : "http://www.receptors.org/nucleardb/",
      "registryIdentifier" : "MIR:00000356",
      "uris" : [ "urn:miriam:nuclearbd", "http://identifiers.org/nuclearbd/", "http://identifiers.org/nuclearbd", "https://identifiers.org/nuclearbd/", "https://identifiers.org/nuclearbd" ]
    },
    "NUCLEOTIDE_SEQUENCE_DATABASE" : {
      "commonName" : "Nucleotide Sequence Database",
      "homepage" : "https://www.ncbi.nlm.nih.gov/Genbank/",
      "registryIdentifier" : "MIR:00000029",
      "uris" : [ "urn:miriam:insdc", "http://identifiers.org/insdc/", "http://identifiers.org/insdc", "https://identifiers.org/insdc/", "https://identifiers.org/insdc" ]
    },
    "OBI" : {
      "commonName" : "Ontology for Biomedical Investigations",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/obi/",
      "registryIdentifier" : "MIR:00000127",
      "uris" : [ "urn:miriam:obi", "urn:miriam:obo.obi", "http://identifiers.org/obi/", "http://identifiers.org/obi", "https://identifiers.org/obi/", "https://identifiers.org/obi" ]
    },
    "ODOR_MOLECULES_DATABASE" : {
      "commonName" : "Odor Molecules DataBase",
      "homepage" : "http://senselab.med.yale.edu/OdorDB",
      "registryIdentifier" : "MIR:00000500",
      "uris" : [ "urn:miriam:odor", "http://identifiers.org/odor/", "http://identifiers.org/odor", "https://identifiers.org/odor/", "https://identifiers.org/odor" ]
    },
    "OLFACTORY_RECEPTOR_DATABASE" : {
      "commonName" : "Olfactory Receptor Database",
      "homepage" : "http://senselab.med.yale.edu/OrDB/",
      "registryIdentifier" : "MIR:00000499",
      "uris" : [ "urn:miriam:ordb", "http://identifiers.org/ordb/", "http://identifiers.org/ordb", "https://identifiers.org/ordb/", "https://identifiers.org/ordb" ]
    },
    "OMA_GROUP" : {
      "commonName" : "OMA Group",
      "homepage" : "https://omabrowser.org/cgi-bin/gateway.pl",
      "registryIdentifier" : "MIR:00000343",
      "uris" : [ "urn:miriam:oma.grp", "http://identifiers.org/oma.grp/", "http://identifiers.org/oma.grp", "https://identifiers.org/oma.grp/", "https://identifiers.org/oma.grp" ]
    },
    "OMA_PROTEIN" : {
      "commonName" : "OMA Protein",
      "homepage" : "https://omabrowser.org/cgi-bin/gateway.pl",
      "registryIdentifier" : "MIR:00000342",
      "uris" : [ "urn:miriam:oma.protein", "http://identifiers.org/oma.protein/", "http://identifiers.org/oma.protein", "https://identifiers.org/oma.protein/", "https://identifiers.org/oma.protein" ]
    },
    "OMIA" : {
      "commonName" : "OMIA",
      "homepage" : "http://omia.angis.org.au/",
      "registryIdentifier" : "MIR:00000142",
      "uris" : [ "urn:miriam:omia", "http://identifiers.org/omia/", "http://identifiers.org/omia", "https://identifiers.org/omia/", "https://identifiers.org/omia" ]
    },
    "OMIM" : {
      "commonName" : "Online Mendelian Inheritance in Man",
      "homepage" : "http://omim.org/",
      "registryIdentifier" : "MIR:00000016",
      "uris" : [ "urn:miriam:omim", "http://identifiers.org/mim/", "http://identifiers.org/mim", "https://identifiers.org/mim/", "https://identifiers.org/mim" ]
    },
    "OMIT" : {
      "commonName" : "OMIT",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/omit/",
      "registryIdentifier" : "MIR:00000605",
      "uris" : [ "http://identifiers.org/omit/", "http://identifiers.org/omit", "https://identifiers.org/omit/", "https://identifiers.org/omit" ]
    },
    "ONTOLOGY_OF_PHYSICS_FOR_BIOLOGY" : {
      "commonName" : "Ontology of Physics for Biology",
      "homepage" : "http://bioportal.bioontology.org/ontologies/OPB",
      "registryIdentifier" : "MIR:00000129",
      "uris" : [ "urn:miriam:opb", "http://identifiers.org/opb/", "http://identifiers.org/opb", "https://identifiers.org/opb/", "https://identifiers.org/opb" ]
    },
    "OPM" : {
      "commonName" : "OPM",
      "homepage" : "http://opm.phar.umich.edu/",
      "registryIdentifier" : "MIR:00000333",
      "uris" : [ "urn:miriam:opm", "http://identifiers.org/opm/", "http://identifiers.org/opm", "https://identifiers.org/opm/", "https://identifiers.org/opm" ]
    },
    "ORCID" : {
      "commonName" : "ORCID",
      "homepage" : "https://orcid.org",
      "registryIdentifier" : "MIR:00000382",
      "uris" : [ "urn:miriam:orcid", "http://identifiers.org/orcid/", "http://identifiers.org/orcid", "https://identifiers.org/orcid/", "https://identifiers.org/orcid" ]
    },
    "ORIDB_SACCHAROMYCES" : {
      "commonName" : "OriDB Saccharomyces",
      "homepage" : "http://cerevisiae.oridb.org/index.php",
      "registryIdentifier" : "MIR:00000369",
      "uris" : [ "urn:miriam:oridb.sacch", "http://identifiers.org/oridb.sacch/", "http://identifiers.org/oridb.sacch", "https://identifiers.org/oridb.sacch/", "https://identifiers.org/oridb.sacch" ]
    },
    "ORIDB_SCHIZOSACCHAROMYCES" : {
      "commonName" : "OriDB Schizosaccharomyces",
      "homepage" : "http://pombe.oridb.org/index.php",
      "registryIdentifier" : "MIR:00000368",
      "uris" : [ "urn:miriam:oridb.schizo", "http://identifiers.org/oridb.schizo/", "http://identifiers.org/oridb.schizo", "https://identifiers.org/oridb.schizo/", "https://identifiers.org/oridb.schizo" ]
    },
    "ORPHANET" : {
      "commonName" : "Orphanet",
      "homepage" : "http://www.orpha.net/consor/",
      "registryIdentifier" : "MIR:00000220",
      "uris" : [ "urn:miriam:orphanet", "http://identifiers.org/orphanet/", "http://identifiers.org/orphanet", "https://identifiers.org/orphanet/", "https://identifiers.org/orphanet" ]
    },
    "ORPHANET_RARE_DISEASE_ONTOLOGY" : {
      "commonName" : "Orphanet Rare Disease Ontology",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/ordo",
      "registryIdentifier" : "MIR:00000532",
      "uris" : [ "urn:miriam:orphanet.ordo", "http://identifiers.org/orphanet.ordo/", "http://identifiers.org/orphanet.ordo", "https://identifiers.org/orphanet.ordo/", "https://identifiers.org/orphanet.ordo" ]
    },
    "ORTHODB" : {
      "commonName" : "OrthoDB",
      "homepage" : "http://cegg.unige.ch/orthodb4",
      "registryIdentifier" : "MIR:00000221",
      "uris" : [ "urn:miriam:orthodb", "http://identifiers.org/orthodb/", "http://identifiers.org/orthodb", "https://identifiers.org/orthodb/", "https://identifiers.org/orthodb" ]
    },
    "ORYZABASE_GENE" : {
      "commonName" : "Oryzabase Gene",
      "homepage" : "http://www.shigen.nig.ac.jp/rice/oryzabaseV4/",
      "registryIdentifier" : "MIR:00000482",
      "uris" : [ "urn:miriam:oryzabase.gene", "http://identifiers.org/oryzabase.gene/", "http://identifiers.org/oryzabase.gene", "https://identifiers.org/oryzabase.gene/", "https://identifiers.org/oryzabase.gene" ]
    },
    "ORYZABASE_MUTANT" : {
      "commonName" : "Oryzabase Mutant",
      "homepage" : "http://www.shigen.nig.ac.jp/rice/oryzabaseV4/",
      "registryIdentifier" : "MIR:00000483",
      "uris" : [ "urn:miriam:oryzabase.mutant", "http://identifiers.org/oryzabase.mutant/", "http://identifiers.org/oryzabase.mutant", "https://identifiers.org/oryzabase.mutant/", "https://identifiers.org/oryzabase.mutant" ]
    },
    "ORYZABASE_STAGE" : {
      "commonName" : "Oryzabase Stage",
      "homepage" : "http://www.shigen.nig.ac.jp/rice/oryzabaseV4/",
      "registryIdentifier" : "MIR:00000485",
      "uris" : [ "urn:miriam:oryzabase.stage", "http://identifiers.org/oryzabase.stage/", "http://identifiers.org/oryzabase.stage", "https://identifiers.org/oryzabase.stage/", "https://identifiers.org/oryzabase.stage" ]
    },
    "ORYZABASE_STRAIN" : {
      "commonName" : "Oryzabase Strain",
      "homepage" : "http://www.shigen.nig.ac.jp/rice/oryzabaseV4/",
      "registryIdentifier" : "MIR:00000484",
      "uris" : [ "urn:miriam:oryzabase.strain", "http://identifiers.org/oryzabase.strain/", "http://identifiers.org/oryzabase.strain", "https://identifiers.org/oryzabase.strain/", "https://identifiers.org/oryzabase.strain" ]
    },
    "ORYZA_TAG_LINE" : {
      "commonName" : "Oryza Tag Line",
      "homepage" : "http://oryzatagline.cirad.fr/",
      "registryIdentifier" : "MIR:00000486",
      "uris" : [ "urn:miriam:otl", "http://identifiers.org/otl/", "http://identifiers.org/otl", "https://identifiers.org/otl/", "https://identifiers.org/otl" ]
    },
    "P3DB_PROTEIN" : {
      "commonName" : "P3DB Protein",
      "homepage" : "http://www.p3db.org/",
      "registryIdentifier" : "MIR:00000501",
      "uris" : [ "urn:miriam:p3db.protein", "http://identifiers.org/p3db.protein/", "http://identifiers.org/p3db.protein", "https://identifiers.org/p3db.protein/", "https://identifiers.org/p3db.protein" ]
    },
    "P3DB_SITE" : {
      "commonName" : "P3DB Site",
      "homepage" : "http://www.p3db.org/",
      "registryIdentifier" : "MIR:00000502",
      "uris" : [ "urn:miriam:p3db.site", "http://identifiers.org/p3db.site/", "http://identifiers.org/p3db.site", "https://identifiers.org/p3db.site/", "https://identifiers.org/p3db.site" ]
    },
    "PALEODB" : {
      "commonName" : "PaleoDB",
      "homepage" : "http://paleodb.org/",
      "registryIdentifier" : "MIR:00000197",
      "uris" : [ "urn:miriam:paleodb", "http://identifiers.org/paleodb/", "http://identifiers.org/paleodb", "https://identifiers.org/paleodb/", "https://identifiers.org/paleodb" ]
    },
    "PANTHER" : {
      "commonName" : "PANTHER Family",
      "homepage" : "http://www.pantherdb.org/",
      "registryIdentifier" : "MIR:00000060",
      "uris" : [ "urn:miriam:panther.family", "urn:miriam:panther", "http://identifiers.org/panther.family/", "http://identifiers.org/panther.family", "https://identifiers.org/panther.family/", "https://identifiers.org/panther.family" ]
    },
    "PANTHER_NODE" : {
      "commonName" : "PANTHER Node",
      "homepage" : "http://pantree.org/",
      "registryIdentifier" : "MIR:00000374",
      "uris" : [ "urn:miriam:panther.node", "http://identifiers.org/panther.node/", "http://identifiers.org/panther.node", "https://identifiers.org/panther.node/", "https://identifiers.org/panther.node" ]
    },
    "PANTHER_PATHWAY" : {
      "commonName" : "PANTHER Pathway",
      "homepage" : "http://www.pantherdb.org/",
      "registryIdentifier" : "MIR:00000363",
      "uris" : [ "urn:miriam:panther.pathway", "http://identifiers.org/panther.pathway/", "http://identifiers.org/panther.pathway", "https://identifiers.org/panther.pathway/", "https://identifiers.org/panther.pathway" ]
    },
    "PANTHER_PATHWAY_COMPONENT" : {
      "commonName" : "PANTHER Pathway Component",
      "homepage" : "http://www.pantherdb.org/",
      "registryIdentifier" : "MIR:00000422",
      "uris" : [ "urn:miriam:panther.pthcmp", "http://identifiers.org/panther.pthcmp/", "http://identifiers.org/panther.pthcmp", "https://identifiers.org/panther.pthcmp/", "https://identifiers.org/panther.pthcmp" ]
    },
    "PASS2" : {
      "commonName" : "PASS2",
      "homepage" : "http://caps.ncbs.res.in/pass2/",
      "registryIdentifier" : "MIR:00000468",
      "uris" : [ "urn:miriam:pass2", "http://identifiers.org/pass2/", "http://identifiers.org/pass2", "https://identifiers.org/pass2/", "https://identifiers.org/pass2" ]
    },
    "PATHWAY_COMMONS" : {
      "commonName" : "Pathway Commons",
      "homepage" : "http://www.pathwaycommons.org/pc/",
      "registryIdentifier" : "MIR:00000073",
      "uris" : [ "urn:miriam:pathwaycommons", "http://identifiers.org/pathwaycommons/", "http://identifiers.org/pathwaycommons", "https://identifiers.org/pathwaycommons/", "https://identifiers.org/pathwaycommons" ]
    },
    "PATHWAY_ONTOLOGY" : {
      "commonName" : "Pathway Ontology",
      "homepage" : "http://rgd.mcw.edu/rgdweb/ontology/search.html",
      "registryIdentifier" : "MIR:00000242",
      "uris" : [ "urn:miriam:pw", "urn:miriam:obo.pw", "http://identifiers.org/pw/", "http://identifiers.org/PW", "https://identifiers.org/pw/", "https://identifiers.org/PW" ]
    },
    "PATO" : {
      "commonName" : "PATO",
      "homepage" : "https://www.ebi.ac.uk/ols/ontologies/pato",
      "registryIdentifier" : "MIR:00000112",
      "uris" : [ "urn:miriam:pato", "urn:miriam:obo.pato", "http://identifiers.org/pato/", "http://identifiers.org/PATO", "https://identifiers.org/pato/", "https://identifiers.org/PATO" ]
    },
    "PAXDB_ORGANISM" : {
      "commonName" : "PaxDb Organism",
      "homepage" : "http://pax-db.org/",
      "registryIdentifier" : "MIR:00000488",
      "uris" : [ "urn:miriam:paxdb.organism", "http://identifiers.org/paxdb.organism/", "http://identifiers.org/paxdb.organism", "https://identifiers.org/paxdb.organism/", "https://identifiers.org/paxdb.organism" ]
    },
    "PAXDB_PROTEIN" : {
      "commonName" : "PaxDb Protein",
      "homepage" : "http://pax-db.org/",
      "registryIdentifier" : "MIR:00000489",
      "uris" : [ "urn:miriam:paxdb.protein", "http://identifiers.org/paxdb.protein/", "http://identifiers.org/paxdb.protein", "https://identifiers.org/paxdb.protein/", "https://identifiers.org/paxdb.protein" ]
    },
    "PAZAR_TRANSCRIPTION_FACTOR" : {
      "commonName" : "Pazar Transcription Factor",
      "homepage" : "http://www.pazar.info/",
      "registryIdentifier" : "MIR:00000306",
      "uris" : [ "urn:miriam:pazar", "http://identifiers.org/pazar/", "http://identifiers.org/pazar", "https://identifiers.org/pazar/", "https://identifiers.org/pazar" ]
    },
    "PDB" : {
      "commonName" : "Protein Data Bank",
      "homepage" : "http://www.pdbe.org/",
      "registryIdentifier" : "MIR:00000020",
      "uris" : [ "urn:miriam:pdb", "http://identifiers.org/pdb/", "http://identifiers.org/pdb", "https://identifiers.org/pdb/", "https://identifiers.org/pdb" ]
    },
    "PDB_CCD" : {
      "commonName" : "Chemical Component Dictionary",
      "homepage" : "https://www.ebi.ac.uk/pdbe-srv/pdbechem/",
      "registryIdentifier" : "MIR:00000113",
      "uris" : [ "urn:miriam:pdb-ccd", "http://identifiers.org/pdb-ccd/", "http://identifiers.org/pdb-ccd", "https://identifiers.org/pdb-ccd/", "https://identifiers.org/pdb-ccd" ]
    },
    "PEPTIDEATLAS" : {
      "commonName" : "PeptideAtlas",
      "homepage" : "http://www.peptideatlas.org/",
      "registryIdentifier" : "MIR:00000053",
      "uris" : [ "urn:miriam:peptideatlas", "http://identifiers.org/peptideatlas/", "http://identifiers.org/peptideatlas", "https://identifiers.org/peptideatlas/", "https://identifiers.org/peptideatlas" ]
    },
    "PEROXIBASE" : {
      "commonName" : "Peroxibase",
      "homepage" : "http://peroxibase.toulouse.inra.fr/",
      "registryIdentifier" : "MIR:00000222",
      "uris" : [ "urn:miriam:peroxibase", "http://identifiers.org/peroxibase/", "http://identifiers.org/peroxibase", "https://identifiers.org/peroxibase/", "https://identifiers.org/peroxibase" ]
    },
    "PFAM" : {
      "commonName" : "Protein Family Database",
      "homepage" : "http://pfam.xfam.org/",
      "registryIdentifier" : "MIR:00000028",
      "uris" : [ "urn:miriam:pfam", "http://identifiers.org/pfam/", "http://identifiers.org/pfam", "https://identifiers.org/pfam/", "https://identifiers.org/pfam" ]
    },
    "PHARM" : {
      "commonName" : "PharmGKB Pathways",
      "homepage" : "http://www.pharmgkb.org/",
      "registryIdentifier" : "MIR:00000089",
      "uris" : [ "urn:miriam:pharmgkb.pathways", "http://identifiers.org/pharmgkb.pathways/", "http://identifiers.org/pharmgkb.pathways", "https://identifiers.org/pharmgkb.pathways/", "https://identifiers.org/pharmgkb.pathways" ]
    },
    "PHARMGKB_DISEASE" : {
      "commonName" : "PharmGKB Disease",
      "homepage" : "http://www.pharmgkb.org/",
      "registryIdentifier" : "MIR:00000090",
      "uris" : [ "urn:miriam:pharmgkb.disease", "http://identifiers.org/pharmgkb.disease/", "http://identifiers.org/pharmgkb.disease", "https://identifiers.org/pharmgkb.disease/", "https://identifiers.org/pharmgkb.disease" ]
    },
    "PHARMGKB_DRUG" : {
      "commonName" : "PharmGKB Drug",
      "homepage" : "http://www.pharmgkb.org/",
      "registryIdentifier" : "MIR:00000091",
      "uris" : [ "urn:miriam:pharmgkb.drug", "http://identifiers.org/pharmgkb.drug/", "http://identifiers.org/pharmgkb.drug", "https://identifiers.org/pharmgkb.drug/", "https://identifiers.org/pharmgkb.drug" ]
    },
    "PHARMGKB_GENE" : {
      "commonName" : "PharmGKB Gene",
      "homepage" : "http://www.pharmgkb.org/",
      "registryIdentifier" : "MIR:00000245",
      "uris" : [ "urn:miriam:pharmgkb.gene", "http://identifiers.org/pharmgkb.gene/", "http://identifiers.org/pharmgkb.gene", "https://identifiers.org/pharmgkb.gene/", "https://identifiers.org/pharmgkb.gene" ]
    },
    "PHENOL_EXPLORER" : {
      "commonName" : "Phenol-Explorer",
      "homepage" : "http://www.phenol-explorer.eu/foods/",
      "registryIdentifier" : "MIR:00000268",
      "uris" : [ "urn:miriam:phenolexplorer", "http://identifiers.org/phenolexplorer/", "http://identifiers.org/phenolexplorer", "https://identifiers.org/phenolexplorer/", "https://identifiers.org/phenolexplorer" ]
    },
    "PHOSPHOPOINT_KINASE" : {
      "commonName" : "PhosphoPoint Kinase",
      "homepage" : "http://kinase.bioinformatics.tw/",
      "registryIdentifier" : "MIR:00000385",
      "uris" : [ "urn:miriam:phosphopoint.kinase", "http://identifiers.org/phosphopoint.kinase/", "http://identifiers.org/phosphopoint.kinase", "https://identifiers.org/phosphopoint.kinase/", "https://identifiers.org/phosphopoint.kinase" ]
    },
    "PHOSPHOPOINT_PHOSPHOPROTEIN" : {
      "commonName" : "PhosphoPoint Phosphoprotein",
      "homepage" : "http://kinase.bioinformatics.tw/",
      "registryIdentifier" : "MIR:00000386",
      "uris" : [ "urn:miriam:phosphopoint.protein", "http://identifiers.org/phosphopoint.protein/", "http://identifiers.org/phosphopoint.protein", "https://identifiers.org/phosphopoint.protein/", "https://identifiers.org/phosphopoint.protein" ]
    },
    "PHOSPHOSITE_PROTEIN" : {
      "commonName" : "PhosphoSite Protein",
      "homepage" : "http://www.phosphosite.org/homeAction.do",
      "registryIdentifier" : "MIR:00000105",
      "uris" : [ "urn:miriam:phosphosite.protein", "urn:miriam:phosphosite", "http://identifiers.org/phosphosite.protein/", "http://identifiers.org/phosphosite.protein", "https://identifiers.org/phosphosite.protein/", "https://identifiers.org/phosphosite.protein" ]
    },
    "PHOSPHOSITE_RESIDUE" : {
      "commonName" : "PhosphoSite Residue",
      "homepage" : "http://www.phosphosite.org/homeAction.do",
      "registryIdentifier" : "MIR:00000125",
      "uris" : [ "urn:miriam:phosphosite.residue", "http://identifiers.org/phosphosite.residue/", "http://identifiers.org/phosphosite.residue", "https://identifiers.org/phosphosite.residue/", "https://identifiers.org/phosphosite.residue" ]
    },
    "PHYLOMEDB" : {
      "commonName" : "PhylomeDB",
      "homepage" : "http://phylomedb.org/",
      "registryIdentifier" : "MIR:00000223",
      "uris" : [ "urn:miriam:phylomedb", "http://identifiers.org/phylomedb/", "http://identifiers.org/phylomedb", "https://identifiers.org/phylomedb/", "https://identifiers.org/phylomedb" ]
    },
    "PHYTOZOME_LOCUS" : {
      "commonName" : "Phytozome Locus",
      "homepage" : "http://www.phytozome.net/",
      "registryIdentifier" : "MIR:00000432",
      "uris" : [ "urn:miriam:phytozome.locus", "http://identifiers.org/phytozome.locus/", "http://identifiers.org/phytozome.locus", "https://identifiers.org/phytozome.locus/", "https://identifiers.org/phytozome.locus" ]
    },
    "PINA" : {
      "commonName" : "PINA",
      "homepage" : "http://cbg.garvan.unsw.edu.au/pina/",
      "registryIdentifier" : "MIR:00000359",
      "uris" : [ "urn:miriam:pina", "http://identifiers.org/pina/", "http://identifiers.org/pina", "https://identifiers.org/pina/", "https://identifiers.org/pina" ]
    },
    "PIROPLASMADB" : {
      "commonName" : "PiroplasmaDB",
      "homepage" : "http://piroplasmadb.org/",
      "registryIdentifier" : "MIR:00000351",
      "uris" : [ "urn:miriam:piroplasma", "http://identifiers.org/piroplasma/", "http://identifiers.org/piroplasma", "https://identifiers.org/piroplasma/", "https://identifiers.org/piroplasma" ]
    },
    "PIRSF" : {
      "commonName" : "PIRSF",
      "homepage" : "https://pir.georgetown.edu/",
      "registryIdentifier" : "MIR:00000017",
      "uris" : [ "urn:miriam:pirsf", "http://identifiers.org/pirsf/", "http://identifiers.org/pirsf", "https://identifiers.org/pirsf/", "https://identifiers.org/pirsf" ]
    },
    "PLANT_ONTOLOGY" : {
      "commonName" : "Plant Ontology",
      "homepage" : "http://www.plantontology.org/",
      "registryIdentifier" : "MIR:00000307",
      "uris" : [ "urn:miriam:po", "urn:miriam:obo.po", "http://identifiers.org/po/", "http://identifiers.org/PO", "https://identifiers.org/po/", "https://identifiers.org/PO" ]
    },
    "PLASMODB" : {
      "commonName" : "PlasmoDB",
      "homepage" : "http://plasmodb.org/plasmo/",
      "registryIdentifier" : "MIR:00000150",
      "uris" : [ "urn:miriam:plasmodb", "http://identifiers.org/plasmodb/", "http://identifiers.org/plasmodb", "https://identifiers.org/plasmodb/", "https://identifiers.org/plasmodb" ]
    },
    "PMC" : {
      "commonName" : "PMC International",
      "homepage" : "http://europepmc.org/",
      "registryIdentifier" : "MIR:00000147",
      "uris" : [ "urn:miriam:pmc", "http://identifiers.org/pmc/", "http://identifiers.org/pmc", "https://identifiers.org/pmc/", "https://identifiers.org/pmc" ]
    },
    "POCKETOME" : {
      "commonName" : "Pocketome",
      "homepage" : "http://www.pocketome.org/sfSearch.cgi?act=browseall",
      "registryIdentifier" : "MIR:00000400",
      "uris" : [ "urn:miriam:pocketome", "http://identifiers.org/pocketome/", "http://identifiers.org/pocketome", "https://identifiers.org/pocketome/", "https://identifiers.org/pocketome" ]
    },
    "POLBASE" : {
      "commonName" : "PolBase",
      "homepage" : "http://polbase.neb.com/",
      "registryIdentifier" : "MIR:00000355",
      "uris" : [ "urn:miriam:polbase", "http://identifiers.org/polbase/", "http://identifiers.org/polbase", "https://identifiers.org/polbase/", "https://identifiers.org/polbase" ]
    },
    "POMBASE" : {
      "commonName" : "PomBase",
      "homepage" : "http://www.pombase.org/",
      "registryIdentifier" : "MIR:00000335",
      "uris" : [ "urn:miriam:pombase", "http://identifiers.org/pombase/", "http://identifiers.org/pombase", "https://identifiers.org/pombase/", "https://identifiers.org/pombase" ]
    },
    "PRIDE" : {
      "commonName" : "PRIDE",
      "homepage" : "https://www.ebi.ac.uk/pride/",
      "registryIdentifier" : "MIR:00000065",
      "uris" : [ "urn:miriam:pride", "http://identifiers.org/pride/", "http://identifiers.org/pride", "https://identifiers.org/pride/", "https://identifiers.org/pride" ]
    },
    "PRIDE_PROJECT" : {
      "commonName" : "PRIDE Project",
      "homepage" : "https://www.ebi.ac.uk/pride/",
      "registryIdentifier" : "MIR:00000515",
      "uris" : [ "urn:miriam:pride.project", "http://identifiers.org/pride.project/", "http://identifiers.org/pride.project", "https://identifiers.org/pride.project/", "https://identifiers.org/pride.project" ]
    },
    "PRINTS" : {
      "commonName" : "PRINTS",
      "homepage" : "http://www.bioinf.manchester.ac.uk/dbbrowser/sprint/",
      "registryIdentifier" : "MIR:00000061",
      "uris" : [ "urn:miriam:sprint", "http://identifiers.org/prints/", "http://identifiers.org/prints", "https://identifiers.org/prints/", "https://identifiers.org/prints" ]
    },
    "PRODOM" : {
      "commonName" : "ProDom",
      "homepage" : "http://prodom.prabi.fr/prodom/current/html/home.php",
      "registryIdentifier" : "MIR:00000117",
      "uris" : [ "urn:miriam:prodom", "http://identifiers.org/prodom/", "http://identifiers.org/prodom", "https://identifiers.org/prodom/", "https://identifiers.org/prodom" ]
    },
    "PROGLYCPROT" : {
      "commonName" : "ProGlycProt",
      "homepage" : "http://www.proglycprot.org/",
      "registryIdentifier" : "MIR:00000354",
      "uris" : [ "urn:miriam:proglyc", "http://identifiers.org/proglyc/", "http://identifiers.org/proglyc", "https://identifiers.org/proglyc/", "https://identifiers.org/proglyc" ]
    },
    "PROSITE" : {
      "commonName" : "PROSITE",
      "homepage" : "https://www.expasy.org/prosite/",
      "registryIdentifier" : "MIR:00000032",
      "uris" : [ "urn:miriam:prosite", "http://identifiers.org/prosite/", "http://identifiers.org/prosite", "https://identifiers.org/prosite/", "https://identifiers.org/prosite" ]
    },
    "PROTCLUSTDB" : {
      "commonName" : "ProtClustDB",
      "homepage" : "https://www.ncbi.nlm.nih.gov/proteinclusters?db=proteinclusters",
      "registryIdentifier" : "MIR:00000226",
      "uris" : [ "urn:miriam:protclustdb", "http://identifiers.org/protclustdb/", "http://identifiers.org/protclustdb", "https://identifiers.org/protclustdb/", "https://identifiers.org/protclustdb" ]
    },
    "PROTEIN_AFFINITY_REAGENTS" : {
      "commonName" : "Protein Affinity Reagents",
      "homepage" : "https://www.ebi.ac.uk/ontology-lookup/browse.do?ontName=PAR",
      "registryIdentifier" : "MIR:00000533",
      "uris" : [ "urn:miriam:psipar", "http://identifiers.org/psipar/", "http://identifiers.org/psipar", "https://identifiers.org/psipar/", "https://identifiers.org/psipar" ]
    },
    "PROTEIN_DATA_BANK_LIGAND" : {
      "commonName" : "Protein Data Bank Ligand",
      "homepage" : "http://www.pdb.org/",
      "registryIdentifier" : "MIR:00000490",
      "uris" : [ "urn:miriam:pdb.ligand", "http://identifiers.org/pdb.ligand/", "http://identifiers.org/pdb.ligand", "https://identifiers.org/pdb.ligand/", "https://identifiers.org/pdb.ligand" ]
    },
    "PROTEIN_MODEL_DATABASE" : {
      "commonName" : "Protein Model Database",
      "homepage" : "https://bioinformatics.cineca.it/PMDB/",
      "registryIdentifier" : "MIR:00000190",
      "uris" : [ "urn:miriam:pmdb", "http://identifiers.org/pmdb/", "http://identifiers.org/pmdb", "https://identifiers.org/pmdb/", "https://identifiers.org/pmdb" ]
    },
    "PROTEIN_ONTOLOGY" : {
      "commonName" : "Protein Ontology",
      "homepage" : "https://proconsortium.org/",
      "registryIdentifier" : "MIR:00000141",
      "uris" : [ "urn:miriam:pr", "urn:miriam:obo.pr", "http://identifiers.org/pr/", "http://identifiers.org/PR", "https://identifiers.org/pr/", "https://identifiers.org/PR" ]
    },
    "PROTEOMICSDB_PEPTIDE" : {
      "commonName" : "ProteomicsDB Peptide",
      "homepage" : "https://www.proteomicsdb.org/#peptideSearch",
      "registryIdentifier" : "MIR:00000525",
      "uris" : [ "urn:miriam:proteomicsdb.peptide", "http://identifiers.org/proteomicsdb.peptide/", "http://identifiers.org/proteomicsdb.peptide", "https://identifiers.org/proteomicsdb.peptide/", "https://identifiers.org/proteomicsdb.peptide" ]
    },
    "PROTEOMICSDB_PROTEIN" : {
      "commonName" : "ProteomicsDB Protein",
      "homepage" : "https://www.proteomicsdb.org/#human",
      "registryIdentifier" : "MIR:00000524",
      "uris" : [ "urn:miriam:proteomicsdb.protein", "http://identifiers.org/proteomicsdb.protein/", "http://identifiers.org/proteomicsdb.protein", "https://identifiers.org/proteomicsdb.protein/", "https://identifiers.org/proteomicsdb.protein" ]
    },
    "PROTONET_CLUSTER" : {
      "commonName" : "ProtoNet Cluster",
      "homepage" : "http://www.protonet.cs.huji.ac.il/",
      "registryIdentifier" : "MIR:00000229",
      "uris" : [ "urn:miriam:protonet.cluster", "http://identifiers.org/protonet.cluster/", "http://identifiers.org/protonet.cluster", "https://identifiers.org/protonet.cluster/", "https://identifiers.org/protonet.cluster" ]
    },
    "PROTONET_PROTEINCARD" : {
      "commonName" : "ProtoNet ProteinCard",
      "homepage" : "http://www.protonet.cs.huji.ac.il/",
      "registryIdentifier" : "MIR:00000228",
      "uris" : [ "urn:miriam:protonet.proteincard", "http://identifiers.org/protonet.proteincard/", "http://identifiers.org/protonet.proteincard", "https://identifiers.org/protonet.proteincard/", "https://identifiers.org/protonet.proteincard" ]
    },
    "PSCDB" : {
      "commonName" : "PSCDB",
      "homepage" : "http://idp1.force.cs.is.nagoya-u.ac.jp/pscdb/index.html",
      "registryIdentifier" : "MIR:00000370",
      "uris" : [ "urn:miriam:pscdb", "http://identifiers.org/pscdb/", "http://identifiers.org/pscdb", "https://identifiers.org/pscdb/", "https://identifiers.org/pscdb" ]
    },
    "PSEUDOMONAS_GENOME_DATABASE" : {
      "commonName" : "Pseudomonas Genome Database",
      "homepage" : "http://www.pseudomonas.com/",
      "registryIdentifier" : "MIR:00000180",
      "uris" : [ "urn:miriam:pseudomonas", "http://identifiers.org/pseudomonas/", "http://identifiers.org/pseudomonas", "https://identifiers.org/pseudomonas/", "https://identifiers.org/pseudomonas" ]
    },
    "PUBCHEM" : {
      "commonName" : "PubChem-compound",
      "homepage" : "http://pubchem.ncbi.nlm.nih.gov/",
      "registryIdentifier" : "MIR:00000034",
      "uris" : [ "urn:miriam:pubchem.compound", "http://identifiers.org/pubchem.compound/", "http://identifiers.org/pubchem.compound", "https://identifiers.org/pubchem.compound/", "https://identifiers.org/pubchem.compound" ]
    },
    "PUBCHEM_BIOASSAY" : {
      "commonName" : "PubChem-bioassay",
      "homepage" : "https://www.ncbi.nlm.nih.gov/sites/entrez?db=pcassay",
      "registryIdentifier" : "MIR:00000072",
      "uris" : [ "urn:miriam:pubchem.bioassay", "http://identifiers.org/pubchem.bioassay/", "http://identifiers.org/pubchem.bioassay", "https://identifiers.org/pubchem.bioassay/", "https://identifiers.org/pubchem.bioassay" ]
    },
    "PUBCHEM_SUBSTANCE" : {
      "commonName" : "PubChem-substance",
      "homepage" : "http://pubchem.ncbi.nlm.nih.gov/",
      "registryIdentifier" : "MIR:00000033",
      "uris" : [ "urn:miriam:pubchem.substance", "http://identifiers.org/pubchem.substance/", "http://identifiers.org/pubchem.substance", "https://identifiers.org/pubchem.substance/", "https://identifiers.org/pubchem.substance" ]
    },
    "PUBMED" : {
      "commonName" : "PubMed",
      "homepage" : "http://www.ncbi.nlm.nih.gov/PubMed/",
      "registryIdentifier" : "MIR:00000015",
      "uris" : [ "urn:miriam:pubmed", "http://identifiers.org/pubmed/", "http://identifiers.org/pubmed", "https://identifiers.org/pubmed/", "https://identifiers.org/pubmed" ]
    },
    "RAT_GENOME_DATABASE_QTL" : {
      "commonName" : "Rat Genome Database qTL",
      "homepage" : "http://rgd.mcw.edu/",
      "registryIdentifier" : "MIR:00000451",
      "uris" : [ "urn:miriam:rgd.qtl", "http://identifiers.org/rgd.qtl/", "http://identifiers.org/rgd.qtl", "https://identifiers.org/rgd.qtl/", "https://identifiers.org/rgd.qtl" ]
    },
    "RAT_GENOME_DATABASE_STRAIN" : {
      "commonName" : "Rat Genome Database strain",
      "homepage" : "http://rgd.mcw.edu/",
      "registryIdentifier" : "MIR:00000452",
      "uris" : [ "urn:miriam:rgd.strain", "http://identifiers.org/rgd.strain/", "http://identifiers.org/rgd.strain", "https://identifiers.org/rgd.strain/", "https://identifiers.org/rgd.strain" ]
    },
    "REACTOME" : {
      "commonName" : "Reactome",
      "homepage" : "http://www.reactome.org/",
      "registryIdentifier" : "MIR:00000018",
      "uris" : [ "urn:miriam:reactome", "http://identifiers.org/reactome/", "http://identifiers.org/reactome", "https://identifiers.org/reactome/", "https://identifiers.org/reactome" ]
    },
    "REBASE" : {
      "commonName" : "REBASE",
      "homepage" : "http://rebase.neb.com/rebase/",
      "registryIdentifier" : "MIR:00000230",
      "uris" : [ "urn:miriam:rebase", "http://identifiers.org/rebase/", "http://identifiers.org/rebase", "https://identifiers.org/rebase/", "https://identifiers.org/rebase" ]
    },
    "REFSEQ" : {
      "commonName" : "RefSeq",
      "homepage" : "http://www.ncbi.nlm.nih.gov/projects/RefSeq/",
      "registryIdentifier" : "MIR:00000039",
      "uris" : [ "urn:miriam:refseq", "http://identifiers.org/refseq/", "http://identifiers.org/refseq", "https://identifiers.org/refseq/", "https://identifiers.org/refseq" ]
    },
    "RELATION_ONTOLOGY" : {
      "commonName" : "Relation Ontology",
      "homepage" : "http://obofoundry.org/ontology/ro.html",
      "registryIdentifier" : "MIR:00000120",
      "uris" : [ "urn:miriam:ro", "urn:miriam:obo.ro", "http://identifiers.org/ro/", "http://identifiers.org/ro", "https://identifiers.org/ro/", "https://identifiers.org/ro" ]
    },
    "RESID" : {
      "commonName" : "RESID",
      "homepage" : "http://pir0.georgetown.edu/resid/",
      "registryIdentifier" : "MIR:00000046",
      "uris" : [ "urn:miriam:resid", "http://identifiers.org/resid/", "http://identifiers.org/resid", "https://identifiers.org/resid/", "https://identifiers.org/resid" ]
    },
    "RFAM" : {
      "commonName" : "RFAM",
      "homepage" : "https://rfam.xfam.org/",
      "registryIdentifier" : "MIR:00000409",
      "uris" : [ "urn:miriam:rfam", "http://identifiers.org/rfam/", "http://identifiers.org/rfam", "https://identifiers.org/rfam/", "https://identifiers.org/rfam" ]
    },
    "RGD" : {
      "commonName" : "Rat Genome Database",
      "homepage" : "http://rgd.mcw.edu/",
      "registryIdentifier" : "MIR:00000047",
      "uris" : [ "urn:miriam:rgd", "http://identifiers.org/rgd/", "http://identifiers.org/rgd", "https://identifiers.org/rgd/", "https://identifiers.org/rgd" ]
    },
    "RHEA" : {
      "commonName" : "Rhea",
      "homepage" : "http://www.rhea-db.org/",
      "registryIdentifier" : "MIR:00000082",
      "uris" : [ "urn:miriam:rhea", "http://identifiers.org/rhea/", "http://identifiers.org/rhea", "https://identifiers.org/rhea/", "https://identifiers.org/rhea" ]
    },
    "RICE_GENOME_ANNOTATION_PROJECT" : {
      "commonName" : "Rice Genome Annotation Project",
      "homepage" : "http://rice.plantbiology.msu.edu/annotation_pseudo_current.shtml",
      "registryIdentifier" : "MIR:00000358",
      "uris" : [ "urn:miriam:ricegap", "http://identifiers.org/ricegap/", "http://identifiers.org/ricegap", "https://identifiers.org/ricegap/", "https://identifiers.org/ricegap" ]
    },
    "RNA_MODIFICATION_DATABASE" : {
      "commonName" : "RNA Modification Database",
      "homepage" : "http://rna-mdb.cas.albany.edu/RNAmods/rnaover.htm",
      "registryIdentifier" : "MIR:00000308",
      "uris" : [ "urn:miriam:rnamods", "http://identifiers.org/rnamods/", "http://identifiers.org/rnamods", "https://identifiers.org/rnamods/", "https://identifiers.org/rnamods" ]
    },
    "ROUGE" : {
      "commonName" : "Rouge",
      "homepage" : "http://www.kazusa.or.jp/rouge/",
      "registryIdentifier" : "MIR:00000293",
      "uris" : [ "urn:miriam:rouge", "http://identifiers.org/rouge/", "http://identifiers.org/rouge", "https://identifiers.org/rouge/", "https://identifiers.org/rouge" ]
    },
    "SABIO_RK_EC_RECORD" : {
      "commonName" : "SABIO-RK EC Record",
      "homepage" : "http://sabiork.h-its.org/",
      "registryIdentifier" : "MIR:00000128",
      "uris" : [ "urn:miriam:sabiork.ec", "http://identifiers.org/sabiork.ec/", "http://identifiers.org/sabiork.ec", "https://identifiers.org/sabiork.ec/", "https://identifiers.org/sabiork.ec" ]
    },
    "SABIO_RK_KINETIC_RECORD" : {
      "commonName" : "SABIO-RK Kinetic Record",
      "homepage" : "http://sabiork.h-its.org/",
      "registryIdentifier" : "MIR:00000086",
      "uris" : [ "urn:miriam:sabiork.kineticrecord", "http://identifiers.org/sabiork.kineticrecord/", "http://identifiers.org/sabiork.kineticrecord", "https://identifiers.org/sabiork.kineticrecord/", "https://identifiers.org/sabiork.kineticrecord" ]
    },
    "SABIO_RK_REACTION" : {
      "commonName" : "SABIO-RK Reaction",
      "homepage" : "http://sabiork.h-its.org/",
      "registryIdentifier" : "MIR:00000038",
      "uris" : [ "urn:miriam:sabiork.reaction", "http://identifiers.org/sabiork.reaction/", "http://identifiers.org/sabiork.reaction", "https://identifiers.org/sabiork.reaction/", "https://identifiers.org/sabiork.reaction" ]
    },
    "SACCHAROMYCES_GENOME_DATABASE_PATHWAYS" : {
      "commonName" : "Saccharomyces genome database pathways",
      "homepage" : "http://pathway.yeastgenome.org/",
      "registryIdentifier" : "MIR:00000057",
      "uris" : [ "urn:miriam:sgd.pathways", "http://identifiers.org/sgd.pathways/", "http://identifiers.org/sgd.pathways", "https://identifiers.org/sgd.pathways/", "https://identifiers.org/sgd.pathways" ]
    },
    "SBML_RDF_VOCABULARY" : {
      "commonName" : "SBML RDF Vocabulary",
      "homepage" : "http://biomodels.net/rdf/vocabulary.rdf",
      "registryIdentifier" : "MIR:00000514",
      "uris" : [ "urn:miriam:biomodels.vocabulary", "http://identifiers.org/biomodels.vocabulary/", "http://identifiers.org/biomodels.vocabulary", "https://identifiers.org/biomodels.vocabulary/", "https://identifiers.org/biomodels.vocabulary" ]
    },
    "SBO_TERM" : {
      "commonName" : "Systems Biology Ontology",
      "homepage" : "http://www.ebi.ac.uk/sbo/main/",
      "registryIdentifier" : "MIR:00000024",
      "uris" : [ "urn:miriam:biomodels.sbo", "urn:miriam:obo.sbo", "urn:miriam:sbo", "http://identifiers.org/biomodels.sbo/", "http://identifiers.org/sbo/", "http://identifiers.org/SBO", "https://identifiers.org/biomodels.sbo/", "https://identifiers.org/sbo/", "https://identifiers.org/SBO" ]
    },
    "SCERTF" : {
      "commonName" : "ScerTF",
      "homepage" : "http://stormo.wustl.edu/ScerTF/",
      "registryIdentifier" : "MIR:00000244",
      "uris" : [ "urn:miriam:scretf", "http://identifiers.org/scretf/", "http://identifiers.org/scretf", "https://identifiers.org/scretf/", "https://identifiers.org/scretf" ]
    },
    "SCOP" : {
      "commonName" : "SCOP",
      "homepage" : "http://scop.mrc-lmb.cam.ac.uk/scop/",
      "registryIdentifier" : "MIR:00000371",
      "uris" : [ "urn:miriam:scop", "http://identifiers.org/scop/", "http://identifiers.org/scop", "https://identifiers.org/scop/", "https://identifiers.org/scop" ]
    },
    "SEED_COMPOUND" : {
      "commonName" : "SEED Compound",
      "homepage" : "http://modelseed.org/",
      "registryIdentifier" : "MIR:00000553",
      "uris" : [ "http://identifiers.org/seed.compound/", "http://identifiers.org/seed.compound", "https://identifiers.org/seed.compound/", "https://identifiers.org/seed.compound" ]
    },
    "SEED_REACTIONS" : {
      "commonName" : "SEED Reactions",
      "homepage" : "http://modelseed.org/biochem/reactions/",
      "registryIdentifier" : "MIR:00000692",
      "uris" : [ "http://identifiers.org/seed.reaction/", "http://identifiers.org/seed.reaction", "https://identifiers.org/seed.reaction/", "https://identifiers.org/seed.reaction" ]
    },
    "SEQUENCE_ONTOLOGY" : {
      "commonName" : "Sequence Ontology",
      "homepage" : "http://www.sequenceontology.org/",
      "registryIdentifier" : "MIR:00000081",
      "uris" : [ "urn:miriam:so", "urn:miriam:obo.so", "http://identifiers.org/so/", "http://identifiers.org/SO", "https://identifiers.org/so/", "https://identifiers.org/SO" ]
    },
    "SEQUENCE_READ_ARCHIVE" : {
      "commonName" : "Sequence Read Archive",
      "homepage" : "https://www.ncbi.nlm.nih.gov/sra",
      "registryIdentifier" : "MIR:00000243",
      "uris" : [ "urn:miriam:insdc.sra", "http://identifiers.org/insdc.sra/", "http://identifiers.org/insdc.sra", "https://identifiers.org/insdc.sra/", "https://identifiers.org/insdc.sra" ]
    },
    "SGD" : {
      "commonName" : "Saccharomyces Genome Database",
      "homepage" : "http://www.yeastgenome.org/",
      "registryIdentifier" : "MIR:00000023",
      "uris" : [ "urn:miriam:sgd", "http://identifiers.org/sgd/", "http://identifiers.org/sgd", "https://identifiers.org/sgd/", "https://identifiers.org/sgd" ]
    },
    "SIDER_DRUG" : {
      "commonName" : "SIDER Drug",
      "homepage" : "http://sideeffects.embl.de/",
      "registryIdentifier" : "MIR:00000435",
      "uris" : [ "urn:miriam:sider.drug", "http://identifiers.org/sider.drug/", "http://identifiers.org/sider.drug", "https://identifiers.org/sider.drug/", "https://identifiers.org/sider.drug" ]
    },
    "SIDER_SIDE_EFFECT" : {
      "commonName" : "SIDER Side Effect",
      "homepage" : "http://sideeffects.embl.de/",
      "registryIdentifier" : "MIR:00000436",
      "uris" : [ "urn:miriam:sider.effect", "http://identifiers.org/sider.effect/", "http://identifiers.org/sider.effect", "https://identifiers.org/sider.effect/", "https://identifiers.org/sider.effect" ]
    },
    "SIGNALING_GATEWAY" : {
      "commonName" : "Signaling Gateway",
      "homepage" : "http://www.signaling-gateway.org/molecule",
      "registryIdentifier" : "MIR:00000045",
      "uris" : [ "urn:miriam:signaling-gateway", "http://identifiers.org/signaling-gateway/", "http://identifiers.org/signaling-gateway", "https://identifiers.org/signaling-gateway/", "https://identifiers.org/signaling-gateway" ]
    },
    "SITEX" : {
      "commonName" : "SitEx",
      "homepage" : "http://www-bionet.sscc.ru/sitex/",
      "registryIdentifier" : "MIR:00000252",
      "uris" : [ "urn:miriam:sitex", "http://identifiers.org/sitex/", "http://identifiers.org/sitex", "https://identifiers.org/sitex/", "https://identifiers.org/sitex" ]
    },
    "SMALL_MOLECULE_PATHWAY_DATABASE" : {
      "commonName" : "Small Molecule Pathway Database",
      "homepage" : "https://smpdb.ca/",
      "registryIdentifier" : "MIR:00000104",
      "uris" : [ "urn:miriam:smpdb", "http://identifiers.org/smpdb/", "http://identifiers.org/smpdb", "https://identifiers.org/smpdb/", "https://identifiers.org/smpdb" ]
    },
    "SMART" : {
      "commonName" : "SMART",
      "homepage" : "http://smart.embl-heidelberg.de/",
      "registryIdentifier" : "MIR:00000118",
      "uris" : [ "urn:miriam:smart", "http://identifiers.org/smart/", "http://identifiers.org/smart", "https://identifiers.org/smart/", "https://identifiers.org/smart" ]
    },
    "SNOMED_CT" : {
      "commonName" : "SNOMED CT",
      "homepage" : "http://www.snomedbrowser.com/",
      "registryIdentifier" : "MIR:00000269",
      "uris" : [ "urn:miriam:snomedct", "http://identifiers.org/snomedct/", "http://identifiers.org/snomedct", "https://identifiers.org/snomedct/", "https://identifiers.org/snomedct" ]
    },
    "SOL_GENOMICS_NETWORK" : {
      "commonName" : "Sol Genomics Network",
      "homepage" : "http://solgenomics.net/",
      "registryIdentifier" : "MIR:00000185",
      "uris" : [ "urn:miriam:sgn", "http://identifiers.org/sgn/", "http://identifiers.org/sgn", "https://identifiers.org/sgn/", "https://identifiers.org/sgn" ]
    },
    "SOYBASE" : {
      "commonName" : "SoyBase",
      "homepage" : "http://soybase.org/",
      "registryIdentifier" : "MIR:00000291",
      "uris" : [ "urn:miriam:soybase", "http://identifiers.org/soybase/", "http://identifiers.org/soybase", "https://identifiers.org/soybase/", "https://identifiers.org/soybase" ]
    },
    "SPECTRAL_DATABASE_FOR_ORGANIC_COMPOUNDS" : {
      "commonName" : "Spectral Database for Organic Compounds",
      "homepage" : "http://riodb01.ibase.aist.go.jp/sdbs/cgi-bin/direct_frame_top.cgi",
      "registryIdentifier" : "MIR:00000319",
      "uris" : [ "urn:miriam:sdbs", "http://identifiers.org/sdbs/", "http://identifiers.org/sdbs", "https://identifiers.org/sdbs/", "https://identifiers.org/sdbs" ]
    },
    "SPIKE" : {
      "commonName" : "SPIKE Map",
      "homepage" : "http://www.cs.tau.ac.il/~spike/",
      "registryIdentifier" : "MIR:00000321",
      "uris" : [ "urn:miriam:spike.map", "http://identifiers.org/spike.map/", "http://identifiers.org/spike.map", "https://identifiers.org/spike.map/", "https://identifiers.org/spike.map" ]
    },
    "STAP" : {
      "commonName" : "STAP",
      "homepage" : "http://psb.kobic.re.kr/STAP/refinement/",
      "registryIdentifier" : "MIR:00000399",
      "uris" : [ "urn:miriam:stap", "http://identifiers.org/stap/", "http://identifiers.org/stap", "https://identifiers.org/stap/", "https://identifiers.org/stap" ]
    },
    "STITCH" : {
      "commonName" : "STITCH",
      "homepage" : "http://stitch.embl.de/",
      "registryIdentifier" : "MIR:00000266",
      "uris" : [ "urn:miriam:stitch", "http://identifiers.org/stitch/", "http://identifiers.org/stitch", "https://identifiers.org/stitch/", "https://identifiers.org/stitch" ]
    },
    "STRING" : {
      "commonName" : "STRING",
      "homepage" : "http://string-db.org/",
      "registryIdentifier" : "MIR:00000265",
      "uris" : [ "urn:miriam:string", "http://identifiers.org/string/", "http://identifiers.org/string", "https://identifiers.org/string/", "https://identifiers.org/string" ]
    },
    "SUBSTRATEDB" : {
      "commonName" : "SubstrateDB",
      "homepage" : "http://substrate.burnham.org/",
      "registryIdentifier" : "MIR:00000224",
      "uris" : [ "urn:miriam:pmap.substratedb", "http://identifiers.org/pmap.substratedb/", "http://identifiers.org/pmap.substratedb", "https://identifiers.org/pmap.substratedb/", "https://identifiers.org/pmap.substratedb" ]
    },
    "SUBTILIST" : {
      "commonName" : "SubtiList",
      "homepage" : "http://genolist.pasteur.fr/SubtiList/",
      "registryIdentifier" : "MIR:00000433",
      "uris" : [ "urn:miriam:subtilist", "http://identifiers.org/subtilist/", "http://identifiers.org/subtilist", "https://identifiers.org/subtilist/", "https://identifiers.org/subtilist" ]
    },
    "SUBTIWIKI" : {
      "commonName" : "SubtiWiki",
      "homepage" : "http://www.subtiwiki.uni-goettingen.de/wiki/index.php/Main_Page",
      "registryIdentifier" : "MIR:00000132",
      "uris" : [ "urn:miriam:subtiwiki", "http://identifiers.org/subtiwiki/", "http://identifiers.org/subtiwiki", "https://identifiers.org/subtiwiki/", "https://identifiers.org/subtiwiki" ]
    },
    "SUPFAM" : {
      "commonName" : "SUPFAM",
      "homepage" : "http://supfam.org/SUPERFAMILY/",
      "registryIdentifier" : "MIR:00000357",
      "uris" : [ "urn:miriam:supfam", "http://identifiers.org/supfam/", "http://identifiers.org/supfam", "https://identifiers.org/supfam/", "https://identifiers.org/supfam" ]
    },
    "SWISS_LIPIDS" : {
      "commonName" : "SwissLipids",
      "homepage" : "http://www.swisslipids.org/#/",
      "registryIdentifier" : "MIR:00000550",
      "uris" : [ "http://identifiers.org/slm/", "http://identifiers.org/SLM", "https://identifiers.org/slm/", "https://identifiers.org/SLM" ]
    },
    "SWISS_MODEL" : {
      "commonName" : "SWISS-MODEL",
      "homepage" : "https://swissmodel.expasy.org",
      "registryIdentifier" : "MIR:00000231",
      "uris" : [ "urn:miriam:swiss-model", "http://identifiers.org/swiss-model/", "http://identifiers.org/swiss-model", "https://identifiers.org/swiss-model/", "https://identifiers.org/swiss-model" ]
    },
    "T3DB" : {
      "commonName" : "T3DB",
      "homepage" : "http://www.t3db.org/",
      "registryIdentifier" : "MIR:00000103",
      "uris" : [ "urn:miriam:t3db", "http://identifiers.org/t3db/", "http://identifiers.org/t3db", "https://identifiers.org/t3db/", "https://identifiers.org/t3db" ]
    },
    "TAIR_GENE" : {
      "commonName" : "TAIR Gene",
      "homepage" : "http://arabidopsis.org/index.jsp",
      "registryIdentifier" : "MIR:00000049",
      "uris" : [ "urn:miriam:tair.gene", "http://identifiers.org/tair.gene/", "http://identifiers.org/tair.gene", "https://identifiers.org/tair.gene/", "https://identifiers.org/tair.gene" ]
    },
    "TAIR_LOCUS" : {
      "commonName" : "TAIR Locus",
      "homepage" : "http://arabidopsis.org/index.jsp",
      "registryIdentifier" : "MIR:00000050",
      "uris" : [ "urn:miriam:tair.locus", "http://identifiers.org/tair.locus/", "http://identifiers.org/tair.locus", "https://identifiers.org/tair.locus/", "https://identifiers.org/tair.locus" ]
    },
    "TAIR_PROTEIN" : {
      "commonName" : "TAIR Protein",
      "homepage" : "http://arabidopsis.org/index.jsp",
      "registryIdentifier" : "MIR:00000048",
      "uris" : [ "urn:miriam:tair.protein", "http://identifiers.org/tair.protein/", "http://identifiers.org/tair.protein", "https://identifiers.org/tair.protein/", "https://identifiers.org/tair.protein" ]
    },
    "TARBASE" : {
      "commonName" : "TarBase",
      "homepage" : "http://diana.imis.athena-innovation.gr/DianaTools/index.php?r=tarbase/index",
      "registryIdentifier" : "MIR:00000340",
      "uris" : [ "urn:miriam:tarbase", "http://identifiers.org/tarbase/", "http://identifiers.org/tarbase", "https://identifiers.org/tarbase/", "https://identifiers.org/tarbase" ]
    },
    "TAXONOMY" : {
      "commonName" : "Taxonomy",
      "homepage" : "http://www.ncbi.nlm.nih.gov/taxonomy/",
      "registryIdentifier" : "MIR:00000006",
      "uris" : [ "urn:miriam:taxonomy", "http://identifiers.org/taxonomy/", "http://identifiers.org/taxonomy", "https://identifiers.org/taxonomy/", "https://identifiers.org/taxonomy" ]
    },
    "TEDDY" : {
      "commonName" : "TEDDY",
      "homepage" : "http://teddyontology.sourceforge.net/",
      "registryIdentifier" : "MIR:00000107",
      "uris" : [ "urn:miriam:biomodels.teddy", "urn:miriam:teddy", "http://identifiers.org/biomodels.teddy/", "http://identifiers.org/biomodels.teddy", "https://identifiers.org/biomodels.teddy/", "https://identifiers.org/biomodels.teddy" ]
    },
    "TETRAHYMENA_GENOME_DATABASE" : {
      "commonName" : "Tetrahymena Genome Database",
      "homepage" : "http://ciliate.org/index.php/",
      "registryIdentifier" : "MIR:00000313",
      "uris" : [ "urn:miriam:tgd", "http://identifiers.org/tgd/", "http://identifiers.org/tgd", "https://identifiers.org/tgd/", "https://identifiers.org/tgd" ]
    },
    "TIGRFAMS" : {
      "commonName" : "TIGRFAMS",
      "homepage" : "http://www.jcvi.org/cgi-bin/tigrfams/Listing.cgi",
      "registryIdentifier" : "MIR:00000315",
      "uris" : [ "urn:miriam:tigrfam", "http://identifiers.org/tigrfam/", "http://identifiers.org/tigrfam", "https://identifiers.org/tigrfam/", "https://identifiers.org/tigrfam" ]
    },
    "TISSUE_LIST" : {
      "commonName" : "Tissue List",
      "homepage" : "https://www.uniprot.org/docs/tisslist.txt",
      "registryIdentifier" : "MIR:00000360",
      "uris" : [ "urn:miriam:tissuelist", "http://identifiers.org/tissuelist/", "http://identifiers.org/tissuelist", "https://identifiers.org/tissuelist/", "https://identifiers.org/tissuelist" ]
    },
    "TOPDB" : {
      "commonName" : "TOPDB",
      "homepage" : "http://topdb.enzim.hu/",
      "registryIdentifier" : "MIR:00000503",
      "uris" : [ "urn:miriam:topdb", "http://identifiers.org/topdb/", "http://identifiers.org/topdb", "https://identifiers.org/topdb/", "https://identifiers.org/topdb" ]
    },
    "TOPFIND" : {
      "commonName" : "TopFind",
      "homepage" : "http://clipserve.clip.ubc.ca/topfind",
      "registryIdentifier" : "MIR:00000255",
      "uris" : [ "urn:miriam:topfind", "http://identifiers.org/topfind/", "http://identifiers.org/topfind", "https://identifiers.org/topfind/", "https://identifiers.org/topfind" ]
    },
    "TOXICOGENOMIC_CHEMICAL" : {
      "commonName" : "Toxicogenomic Chemical",
      "homepage" : "http://ctdbase.org/",
      "registryIdentifier" : "MIR:00000098",
      "uris" : [ "urn:miriam:ctd.chemical", "http://identifiers.org/ctd.chemical/", "http://identifiers.org/ctd.chemical", "https://identifiers.org/ctd.chemical/", "https://identifiers.org/ctd.chemical" ]
    },
    "TOXODB" : {
      "commonName" : "ToxoDB",
      "homepage" : "http://toxodb.org/toxo/",
      "registryIdentifier" : "MIR:00000153",
      "uris" : [ "urn:miriam:toxoplasma", "http://identifiers.org/toxoplasma/", "http://identifiers.org/toxoplasma", "https://identifiers.org/toxoplasma/", "https://identifiers.org/toxoplasma" ]
    },
    "TRANSPORT_CLASSIFICATION_DATABASE" : {
      "commonName" : "Transport Classification Database",
      "homepage" : "http://www.tcdb.org/",
      "registryIdentifier" : "MIR:00000040",
      "uris" : [ "urn:miriam:tcdb", "http://identifiers.org/tcdb/", "http://identifiers.org/tcdb", "https://identifiers.org/tcdb/", "https://identifiers.org/tcdb" ]
    },
    "TREEBASE" : {
      "commonName" : "TreeBASE",
      "homepage" : "http://treebase.org/",
      "registryIdentifier" : "MIR:00000312",
      "uris" : [ "urn:miriam:treebase", "http://identifiers.org/treebase/", "http://identifiers.org/treebase", "https://identifiers.org/treebase/", "https://identifiers.org/treebase" ]
    },
    "TREEFAM" : {
      "commonName" : "TreeFam",
      "homepage" : "http://www.treefam.org/",
      "registryIdentifier" : "MIR:00000395",
      "uris" : [ "urn:miriam:treefam", "http://identifiers.org/treefam/", "http://identifiers.org/treefam", "https://identifiers.org/treefam/", "https://identifiers.org/treefam" ]
    },
    "TREE_OF_LIFE" : {
      "commonName" : "Tree of Life",
      "homepage" : "http://tolweb.org/tree/",
      "registryIdentifier" : "MIR:00000405",
      "uris" : [ "urn:miriam:tol", "http://identifiers.org/tol/", "http://identifiers.org/tol", "https://identifiers.org/tol/", "https://identifiers.org/tol" ]
    },
    "TRICHDB" : {
      "commonName" : "TrichDB",
      "homepage" : "http://trichdb.org/trichdb/",
      "registryIdentifier" : "MIR:00000154",
      "uris" : [ "urn:miriam:trichdb", "http://identifiers.org/trichdb/", "http://identifiers.org/trichdb", "https://identifiers.org/trichdb/", "https://identifiers.org/trichdb" ]
    },
    "TRITRYPDB" : {
      "commonName" : "TriTrypDB",
      "homepage" : "http://tritrypdb.org/tritrypdb/",
      "registryIdentifier" : "MIR:00000155",
      "uris" : [ "urn:miriam:tritrypdb", "http://identifiers.org/tritrypdb/", "http://identifiers.org/tritrypdb", "https://identifiers.org/tritrypdb/", "https://identifiers.org/tritrypdb" ]
    },
    "TTD_Drug" : {
      "commonName" : "TTD Drug",
      "homepage" : "http://bidd.nus.edu.sg/group/ttd/ttd.asp",
      "registryIdentifier" : "MIR:00000092",
      "uris" : [ "urn:miriam:ttd.drug", "http://identifiers.org/ttd.drug/", "http://identifiers.org/ttd.drug", "https://identifiers.org/ttd.drug/", "https://identifiers.org/ttd.drug" ]
    },
    "TTD_TARGET" : {
      "commonName" : "TTD Target",
      "homepage" : "http://bidd.nus.edu.sg/group/ttd/ttd.asp",
      "registryIdentifier" : "MIR:00000093",
      "uris" : [ "urn:miriam:ttd.target", "http://identifiers.org/ttd.target/", "http://identifiers.org/ttd.target", "https://identifiers.org/ttd.target/", "https://identifiers.org/ttd.target" ]
    },
    "UBERON" : {
      "commonName" : "UBERON",
      "homepage" : "http://bioportal.bioontology.org/ontologies/UBERON",
      "registryIdentifier" : "MIR:00000446",
      "uris" : [ "urn:miriam:uberon", "http://identifiers.org/uberon/", "http://identifiers.org/UBERON", "https://identifiers.org/uberon/", "https://identifiers.org/UBERON" ]
    },
    "UBIO_NAMEBANK" : {
      "commonName" : "uBio NameBank",
      "homepage" : "http://www.ubio.org",
      "registryIdentifier" : "MIR:00000338",
      "uris" : [ "urn:miriam:ubio.namebank", "http://identifiers.org/ubio.namebank/", "http://identifiers.org/ubio.namebank", "https://identifiers.org/ubio.namebank/", "https://identifiers.org/ubio.namebank" ]
    },
    "UM_BBD_BIOTRANSFORMATION_RULE" : {
      "commonName" : "UM-BBD Biotransformation Rule",
      "homepage" : "http://umbbd.ethz.ch/servlets/pageservlet?ptype=allrules",
      "registryIdentifier" : "MIR:00000328",
      "uris" : [ "urn:miriam:umbbd.rule", "http://identifiers.org/umbbd.rule/", "http://identifiers.org/umbbd.rule", "https://identifiers.org/umbbd.rule/", "https://identifiers.org/umbbd.rule" ]
    },
    "UM_BBD_COMPOUND" : {
      "commonName" : "UM-BBD Compound",
      "homepage" : "http://umbbd.ethz.ch/",
      "registryIdentifier" : "MIR:00000276",
      "uris" : [ "urn:miriam:umbbd.compound", "http://identifiers.org/umbbd.compound/", "http://identifiers.org/umbbd.compound", "https://identifiers.org/umbbd.compound/", "https://identifiers.org/umbbd.compound" ]
    },
    "UM_BBD_ENZYME" : {
      "commonName" : "UM-BBD Enzyme",
      "homepage" : "http://umbbd.ethz.ch/",
      "registryIdentifier" : "MIR:00000326",
      "uris" : [ "urn:miriam:umbbd.enzyme", "http://identifiers.org/umbbd.enzyme/", "http://identifiers.org/umbbd.enzyme", "https://identifiers.org/umbbd.enzyme/", "https://identifiers.org/umbbd.enzyme" ]
    },
    "UM_BBD_PATHWAY" : {
      "commonName" : "UM-BBD Pathway",
      "homepage" : "http://umbbd.ethz.ch/",
      "registryIdentifier" : "MIR:00000327",
      "uris" : [ "urn:miriam:umbbd.pathway", "http://identifiers.org/umbbd.pathway/", "http://identifiers.org/umbbd.pathway", "https://identifiers.org/umbbd.pathway/", "https://identifiers.org/umbbd.pathway" ]
    },
    "UM_BBD_REACTION" : {
      "commonName" : "UM-BBD Reaction",
      "homepage" : "http://umbbd.ethz.ch/",
      "registryIdentifier" : "MIR:00000325",
      "uris" : [ "urn:miriam:umbbd.reaction", "http://identifiers.org/umbbd.reaction/", "http://identifiers.org/umbbd.reaction", "https://identifiers.org/umbbd.reaction/", "https://identifiers.org/umbbd.reaction" ]
    },
    "UNIGENE" : {
      "commonName" : "UniGene",
      "homepage" : "http://www.ncbi.nlm.nih.gov/unigene",
      "registryIdentifier" : "MIR:00000346",
      "uris" : [ "urn:miriam:unigene", "http://identifiers.org/unigene/", "http://identifiers.org/unigene", "https://identifiers.org/unigene/", "https://identifiers.org/unigene" ]
    },
    "UNII" : {
      "commonName" : "UNII",
      "homepage" : "http://fdasis.nlm.nih.gov/srs/",
      "registryIdentifier" : "MIR:00000531",
      "uris" : [ "urn:miriam:unii", "http://identifiers.org/unii/", "http://identifiers.org/unii", "https://identifiers.org/unii/", "https://identifiers.org/unii" ]
    },
    "UNIMOD" : {
      "commonName" : "Unimod",
      "homepage" : "http://www.unimod.org/",
      "registryIdentifier" : "MIR:00000447",
      "uris" : [ "urn:miriam:unimod", "http://identifiers.org/unimod/", "http://identifiers.org/unimod", "https://identifiers.org/unimod/", "https://identifiers.org/unimod" ]
    },
    "UNIPARC" : {
      "commonName" : "UniParc",
      "homepage" : "https://www.ebi.ac.uk/uniparc/",
      "registryIdentifier" : "MIR:00000041",
      "uris" : [ "urn:miriam:uniparc", "http://identifiers.org/uniparc/", "http://identifiers.org/uniparc", "https://identifiers.org/uniparc/", "https://identifiers.org/uniparc" ]
    },
    "UNIPATHWAY_REACTION" : {
      "commonName" : "UniPathway Reaction",
      "homepage" : "http://www.grenoble.prabi.fr/obiwarehouse/unipathway/",
      "registryIdentifier" : "MIR:00000570",
      "uris" : [ "http://identifiers.org/unipathway.reaction/", "http://identifiers.org/unipathway.reaction", "https://identifiers.org/unipathway.reaction/", "https://identifiers.org/unipathway.reaction" ]
    },
    "UNIPROT" : {
      "commonName" : "Uniprot",
      "homepage" : "http://www.uniprot.org/",
      "registryIdentifier" : "MIR:00000005",
      "uris" : [ "urn:miriam:uniprot", "urn:lsid:uniprot.org", "http://identifiers.org/uniprot/", "http://identifiers.org/uniprot", "https://purl.uniprot.org/uniprot/", "https://identifiers.org/uniprot/", "https://identifiers.org/uniprot" ]
    },
    "UNIPROT_ISOFORM" : {
      "commonName" : "UniProt Isoform",
      "homepage" : "http://www.uniprot.org/",
      "registryIdentifier" : "MIR:00000388",
      "uris" : [ "urn:miriam:uniprot.isoform", "http://identifiers.org/uniprot.isoform/", "http://identifiers.org/uniprot.isoform", "https://identifiers.org/uniprot.isoform/", "https://identifiers.org/uniprot.isoform" ]
    },
    "UNISTS" : {
      "commonName" : "UniSTS",
      "homepage" : "https://www.ncbi.nlm.nih.gov/sites/entrez?db=unists",
      "registryIdentifier" : "MIR:00000162",
      "uris" : [ "urn:miriam:unists", "http://identifiers.org/unists/", "http://identifiers.org/unists", "https://identifiers.org/unists/", "https://identifiers.org/unists" ]
    },
    "UNITE" : {
      "commonName" : "Unite",
      "homepage" : "http://unite.ut.ee/",
      "registryIdentifier" : "MIR:00000352",
      "uris" : [ "urn:miriam:unite", "http://identifiers.org/unite/", "http://identifiers.org/unite", "https://identifiers.org/unite/", "https://identifiers.org/unite" ]
    },
    "UNIT_ONTOLOGY" : {
      "commonName" : "Unit Ontology",
      "homepage" : "http://bioportal.bioontology.org/ontologies/UO",
      "registryIdentifier" : "MIR:00000136",
      "uris" : [ "urn:miriam:unit", "urn:miriam:obo.unit", "http://identifiers.org/uo/", "http://identifiers.org/UO", "https://identifiers.org/uo/", "https://identifiers.org/UO" ]
    },
    "UNKNOWN" : {
      "commonName" : "Unknown",
      "homepage" : null,
      "registryIdentifier" : null,
      "uris" : [ ]
    },
    "USPTO" : {
      "commonName" : "USPTO",
      "homepage" : "http://patft.uspto.gov/netahtml/PTO/index.html",
      "registryIdentifier" : "MIR:00000538",
      "uris" : [ "urn:miriam:uspto", "http://identifiers.org/uspto/", "http://identifiers.org/uspto", "https://identifiers.org/uspto/", "https://identifiers.org/uspto" ]
    },
    "VARIO" : {
      "commonName" : "VariO",
      "homepage" : "http://bioportal.bioontology.org/ontologies/VARIO",
      "registryIdentifier" : "MIR:00000406",
      "uris" : [ "urn:miriam:vario", "http://identifiers.org/vario/", "http://identifiers.org/VariO", "https://identifiers.org/vario/", "https://identifiers.org/VariO" ]
    },
    "VBASE2" : {
      "commonName" : "Vbase2",
      "homepage" : "http://www.vbase2.org/vbase2.php",
      "registryIdentifier" : "MIR:00000320",
      "uris" : [ "urn:miriam:vbase2", "http://identifiers.org/vbase2/", "http://identifiers.org/vbase2", "https://identifiers.org/vbase2/", "https://identifiers.org/vbase2" ]
    },
    "VBRC" : {
      "commonName" : "VBRC",
      "homepage" : "http://vbrc.org/",
      "registryIdentifier" : "MIR:00000448",
      "uris" : [ "urn:miriam:vbrc", "http://identifiers.org/vbrc/", "http://identifiers.org/vbrc", "https://identifiers.org/vbrc/", "https://identifiers.org/vbrc" ]
    },
    "VFDB_GENE" : {
      "commonName" : "VFDB Gene",
      "homepage" : "http://www.mgc.ac.cn/VFs/",
      "registryIdentifier" : "MIR:00000472",
      "uris" : [ "urn:miriam:vfdb.gene", "http://identifiers.org/vfdb.gene/", "http://identifiers.org/vfdb.gene", "https://identifiers.org/vfdb.gene/", "https://identifiers.org/vfdb.gene" ]
    },
    "VFDB_GENUS" : {
      "commonName" : "VFDB Genus",
      "homepage" : "http://www.mgc.ac.cn/VFs/",
      "registryIdentifier" : "MIR:00000471",
      "uris" : [ "urn:miriam:vfdb.genus", "http://identifiers.org/vfdb.genus/", "http://identifiers.org/vfdb.genus", "https://identifiers.org/vfdb.genus/", "https://identifiers.org/vfdb.genus" ]
    },
    "VIRALZONE" : {
      "commonName" : "ViralZone",
      "homepage" : "http://www.expasy.org/viralzone/",
      "registryIdentifier" : "MIR:00000449",
      "uris" : [ "urn:miriam:viralzone", "http://identifiers.org/viralzone/", "http://identifiers.org/viralzone", "https://identifiers.org/viralzone/", "https://identifiers.org/viralzone" ]
    },
    "VIRSIRNA" : {
      "commonName" : "VIRsiRNA",
      "homepage" : "http://crdd.osdd.net/servers/virsirnadb",
      "registryIdentifier" : "MIR:00000249",
      "uris" : [ "urn:miriam:virsirna", "http://identifiers.org/virsirna/", "http://identifiers.org/virsirna", "https://identifiers.org/virsirna/", "https://identifiers.org/virsirna" ]
    },
    "VMH_METABOLITE" : {
      "commonName" : "VMH metabolite",
      "homepage" : "https://vmh.uni.lu/",
      "registryIdentifier" : "MIR:00000636",
      "uris" : [ "urn:miriam:vmhmetabolite", "http://identifiers.org/vmhmetabolite/", "http://identifiers.org/vmhmetabolite", "https://identifiers.org/vmhmetabolite/", "https://identifiers.org/vmhmetabolite" ]
    },
    "VMH_REACTION" : {
      "commonName" : "VMH reaction",
      "homepage" : "https://vmh.uni.lu/",
      "registryIdentifier" : "MIR:00000640",
      "uris" : [ "urn:miriam:vmhreaction", "http://identifiers.org/vmhreaction/", "http://identifiers.org/vmhreaction", "https://identifiers.org/vmhreaction/", "https://identifiers.org/vmhreaction" ]
    },
    "WIKIDATA" : {
      "commonName" : "Wikidata",
      "homepage" : "https://www.wikidata.org/",
      "registryIdentifier" : "MIR:00000549",
      "uris" : [ "urn:miriam:wikidata", "http://identifiers.org/wikidata/", "http://identifiers.org/wikidata", "https://identifiers.org/wikidata/", "https://identifiers.org/wikidata" ]
    },
    "WIKIGENES" : {
      "commonName" : "WikiGenes",
      "homepage" : "http://www.wikigenes.org/",
      "registryIdentifier" : "MIR:00000437",
      "uris" : [ "urn:miriam:wikigenes", "http://identifiers.org/wikigenes/", "http://identifiers.org/wikigenes", "https://identifiers.org/wikigenes/", "https://identifiers.org/wikigenes" ]
    },
    "WIKIPATHWAYS" : {
      "commonName" : "WikiPathways",
      "homepage" : "http://www.wikipathways.org/",
      "registryIdentifier" : "MIR:00000076",
      "uris" : [ "urn:miriam:wikipathways", "http://identifiers.org/wikipathways/", "http://identifiers.org/wikipathways", "https://identifiers.org/wikipathways/", "https://identifiers.org/wikipathways" ]
    },
    "WIKIPEDIA" : {
      "commonName" : "Wikipedia (English)",
      "homepage" : "http://en.wikipedia.org/wiki/Main_Page",
      "registryIdentifier" : "MIR:00000384",
      "uris" : [ "urn:miriam:wikipedia.en", "http://identifiers.org/wikipedia.en/", "http://identifiers.org/wikipedia.en", "https://identifiers.org/wikipedia.en/", "https://identifiers.org/wikipedia.en" ]
    },
    "WORFDB" : {
      "commonName" : "Worfdb",
      "homepage" : "http://worfdb.dfci.harvard.edu/",
      "registryIdentifier" : "MIR:00000288",
      "uris" : [ "urn:miriam:worfdb", "http://identifiers.org/worfdb/", "http://identifiers.org/worfdb", "https://identifiers.org/worfdb/", "https://identifiers.org/worfdb" ]
    },
    "WORMPEP" : {
      "commonName" : "Wormpep",
      "homepage" : "https://www.wormbase.org/db/seq/protein",
      "registryIdentifier" : "MIR:00000031",
      "uris" : [ "urn:miriam:wormpep", "http://identifiers.org/wormpep/", "http://identifiers.org/wormpep", "https://identifiers.org/wormpep/", "https://identifiers.org/wormpep" ]
    },
    "WORM_BASE" : {
      "commonName" : "WormBase",
      "homepage" : "http://wormbase.bio2rdf.org/fct",
      "registryIdentifier" : "MIR:00000027",
      "uris" : [ "urn:miriam:wormbase", "http://identifiers.org/wb/", "http://identifiers.org/wb", "https://identifiers.org/wb/", "https://identifiers.org/wb" ]
    },
    "WORM_BASE_RNAI" : {
      "commonName" : "WormBase RNAi",
      "homepage" : "https://www.wormbase.org/",
      "registryIdentifier" : "MIR:00000466",
      "uris" : [ "urn:miriam:wormbase.rnai", "http://identifiers.org/wb.rnai/", "http://identifiers.org/wb.rnai", "https://identifiers.org/wb.rnai/", "https://identifiers.org/wb.rnai" ]
    },
    "XENBASE" : {
      "commonName" : "Xenbase",
      "homepage" : "https://www.xenbase.org/",
      "registryIdentifier" : "MIR:00000186",
      "uris" : [ "urn:miriam:xenbase", "http://identifiers.org/xenbase/", "http://identifiers.org/xenbase", "https://identifiers.org/xenbase/", "https://identifiers.org/xenbase" ]
    },
    "YDPM" : {
      "commonName" : "YDPM",
      "homepage" : "http://www-deletion.stanford.edu/YDPM/",
      "registryIdentifier" : "MIR:00000465",
      "uris" : [ "urn:miriam:ydpm", "http://identifiers.org/ydpm/", "http://identifiers.org/ydpm", "https://identifiers.org/ydpm/", "https://identifiers.org/ydpm" ]
    },
    "YEAST_INTRON_DATABASE_V3" : {
      "commonName" : "Yeast Intron Database v3",
      "homepage" : "http://compbio.soe.ucsc.edu/yeast_introns.html",
      "registryIdentifier" : "MIR:00000460",
      "uris" : [ "urn:miriam:yid", "http://identifiers.org/yid/", "http://identifiers.org/yid", "https://identifiers.org/yid/", "https://identifiers.org/yid" ]
    },
    "YEAST_INTRON_DATABASE_V4_3" : {
      "commonName" : "Yeast Intron Database v4.3",
      "homepage" : "http://intron.ucsc.edu/yeast4.3/",
      "registryIdentifier" : "MIR:00000521",
      "uris" : [ "urn:miriam:yeastintron", "http://identifiers.org/yeastintron/", "http://identifiers.org/yeastintron", "https://identifiers.org/yeastintron/", "https://identifiers.org/yeastintron" ]
    },
    "YETFASCO" : {
      "commonName" : "YeTFasCo",
      "homepage" : "http://yetfasco.ccbr.utoronto.ca/",
      "registryIdentifier" : "MIR:00000339",
      "uris" : [ "urn:miriam:yetfasco", "http://identifiers.org/yetfasco/", "http://identifiers.org/yetfasco", "https://identifiers.org/yetfasco/", "https://identifiers.org/yetfasco" ]
    },
    "YRC_PDR" : {
      "commonName" : "YRC PDR",
      "homepage" : "http://www.yeastrc.org/pdr/",
      "registryIdentifier" : "MIR:00000459",
      "uris" : [ "urn:miriam:yrcpdr", "http://identifiers.org/yrcpdr/", "http://identifiers.org/yrcpdr", "https://identifiers.org/yrcpdr/", "https://identifiers.org/yrcpdr" ]
    },
    "ZFIN" : {
      "commonName" : "ZFIN Bioentity",
      "homepage" : "http://zfin.org",
      "registryIdentifier" : "MIR:00000079",
      "uris" : [ "urn:miriam:zfin", "http://identifiers.org/zfin/", "http://identifiers.org/zfin", "https://identifiers.org/zfin/", "https://identifiers.org/zfin" ]
    },
    "ZINC" : {
      "commonName" : "ZINC",
      "homepage" : "http://zinc15.docking.org/",
      "registryIdentifier" : "MIR:00000529",
      "uris" : [ "urn:miriam:zinc", "http://identifiers.org/zinc/", "http://identifiers.org/zinc", "https://identifiers.org/zinc/", "https://identifiers.org/zinc" ]
    },
    "_3DMET" : {
      "commonName" : "3DMET",
      "homepage" : "http://www.3dmet.dna.affrc.go.jp/",
      "registryIdentifier" : " MIR:00000066",
      "uris" : [ "urn:miriam:3dmet", "http://identifiers.org/3dmet/", "http://identifiers.org/3dmet", "https://identifiers.org/3dmet/", "https://identifiers.org/3dmet" ]
    }
  },
  "mapTypes" : [ {
    "name" : "Downstream targets",
    "id" : "DOWNSTREAM_TARGETS"
  }, {
    "name" : "Pathway",
    "id" : "PATHWAY"
  }, {
    "name" : "Unknown",
    "id" : "UNKNOWN"
  } ],
  "unitTypes" : [ {
    "name" : "ampere",
    "id" : "AMPERE"
  }, {
    "name" : "avogadro",
    "id" : "AVOGADRO"
  }, {
    "name" : "becquerel",
    "id" : "BECQUEREL"
  }, {
    "name" : "candela",
    "id" : "CANDELA"
  }, {
    "name" : "coulumb",
    "id" : "COULUMB"
  }, {
    "name" : "dimensionless",
    "id" : "DIMENSIONLESS"
  }, {
    "name" : "farad",
    "id" : "FARAD"
  }, {
    "name" : "gram",
    "id" : "GRAM"
  }, {
    "name" : "gray",
    "id" : "GRAY"
  }, {
    "name" : "henry",
    "id" : "HENRY"
  }, {
    "name" : "hertz",
    "id" : "HERTZ"
  }, {
    "name" : "item",
    "id" : "ITEM"
  }, {
    "name" : "joule",
    "id" : "JOULE"
  }, {
    "name" : "katal",
    "id" : "KATAL"
  }, {
    "name" : "kelvin",
    "id" : "KELVIN"
  }, {
    "name" : "kilogram",
    "id" : "KILOGRAM"
  }, {
    "name" : "litre",
    "id" : "LITRE"
  }, {
    "name" : "lumen",
    "id" : "LUMEN"
  }, {
    "name" : "lux",
    "id" : "LUX"
  }, {
    "name" : "metre",
    "id" : "METRE"
  }, {
    "name" : "mole",
    "id" : "MOLE"
  }, {
    "name" : "newton",
    "id" : "NEWTON"
  }, {
    "name" : "ohm",
    "id" : "OHM"
  }, {
    "name" : "pascal",
    "id" : "PASCAL"
  }, {
    "name" : "radian",
    "id" : "RADIAN"
  }, {
    "name" : "second",
    "id" : "SECOND"
  }, {
    "name" : "siemens",
    "id" : "SIEMENS"
  }, {
    "name" : "sievert",
    "id" : "SIEVERT"
  }, {
    "name" : "steradian",
    "id" : "STERADIAN"
  }, {
    "name" : "tesla",
    "id" : "TESLA"
  }, {
    "name" : "volt",
    "id" : "VOLT"
  }, {
    "name" : "watt",
    "id" : "WATT"
  }, {
    "name" : "weber",
    "id" : "WEBER"
  } ],
  "modificationStateTypes" : {
    "ACETYLATED" : {
      "commonName" : "acetylated",
      "abbreviation" : "Ac"
    },
    "DONT_CARE" : {
      "commonName" : "unspecified",
      "abbreviation" : "*"
    },
    "EMPTY" : {
      "commonName" : "empty",
      "abbreviation" : ""
    },
    "GLYCOSYLATED" : {
      "commonName" : "glycosylated",
      "abbreviation" : "G"
    },
    "HYDROXYLATED" : {
      "commonName" : "hydroxylated",
      "abbreviation" : "OH"
    },
    "METHYLATED" : {
      "commonName" : "methylated",
      "abbreviation" : "Me"
    },
    "MYRISTOYLATED" : {
      "commonName" : "myristoylated",
      "abbreviation" : "My"
    },
    "PALMYTOYLATED" : {
      "commonName" : "palmytoylated",
      "abbreviation" : "Pa"
    },
    "PHOSPHORYLATED" : {
      "commonName" : "phosphorylated",
      "abbreviation" : "P"
    },
    "PRENYLATED" : {
      "commonName" : "prenylated",
      "abbreviation" : "Pr"
    },
    "PROTONATED" : {
      "commonName" : "protonated",
      "abbreviation" : "H"
    },
    "SULFATED" : {
      "commonName" : "sulfated",
      "abbreviation" : "S"
    },
    "UBIQUITINATED" : {
      "commonName" : "ubiquitinated",
      "abbreviation" : "Ub"
    },
    "UNKNOWN" : {
      "commonName" : "unknown",
      "abbreviation" : "?"
    }
  },
  "privilegeTypes" : {
    "IS_ADMIN" : {
      "commonName" : "Admin",
      "objectType" : null,
      "valueType" : "boolean"
    },
    "IS_CURATOR" : {
      "commonName" : "Curator",
      "objectType" : null,
      "valueType" : "boolean"
    },
    "READ_PROJECT" : {
      "commonName" : "View project",
      "objectType" : "Project",
      "valueType" : "boolean"
    },
    "WRITE_PROJECT" : {
      "commonName" : "Modify project",
      "objectType" : "Project",
      "valueType" : "boolean"
    }
  },
  "version" : "Unknown",
  "buildDate" : "Unknown",
  "gitHash" : "Unknown",
  "annotators" : [ {
    "className" : "lcsb.mapviewer.annotation.services.annotators.PdbAnnotator",
    "name" : "Protein Data Bank",
    "description" : "",
    "url" : "http://www.pdbe.org/",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Rna", "lcsb.mapviewer.model.map.species.Gene" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "UNIPROT",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "PDB",
      "order" : 1,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.TairAnnotator",
    "name" : "TAIR",
    "description" : "",
    "url" : "http://arabidopsis.org/index.jsp",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Gene", "lcsb.mapviewer.model.map.species.Rna" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "TAIR_LOCUS",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "UNIPROT",
      "order" : 1,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.ChebiAnnotator",
    "name" : "Chebi",
    "description" : "",
    "url" : "http://www.ebi.ac.uk/chebi/",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Chemical" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "CHEBI",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : "NAME",
      "annotation_type" : null,
      "order" : 1,
      "type" : "INPUT"
    }, {
      "field" : "FULL_NAME",
      "annotation_type" : null,
      "order" : 2,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "INCHI",
      "order" : 3,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "INCHIKEY",
      "order" : 4,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "STITCH",
      "order" : 5,
      "type" : "OUTPUT"
    }, {
      "field" : "SMILE",
      "annotation_type" : null,
      "order" : 6,
      "type" : "OUTPUT"
    }, {
      "field" : "SYNONYMS",
      "annotation_type" : null,
      "order" : 7,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.EntrezAnnotator",
    "name" : "Entrez Gene",
    "description" : "",
    "url" : "http://www.ncbi.nlm.nih.gov/gene",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Rna", "lcsb.mapviewer.model.map.species.Gene" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "ENTREZ",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "ENSEMBL",
      "order" : 1,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "HGNC",
      "order" : 2,
      "type" : "OUTPUT"
    }, {
      "field" : "FULL_NAME",
      "annotation_type" : null,
      "order" : 3,
      "type" : "OUTPUT"
    }, {
      "field" : "DESCRIPTION",
      "annotation_type" : null,
      "order" : 4,
      "type" : "OUTPUT"
    }, {
      "field" : "SYMBOL",
      "annotation_type" : null,
      "order" : 5,
      "type" : "OUTPUT"
    }, {
      "field" : "SYNONYMS",
      "annotation_type" : null,
      "order" : 6,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.BrendaAnnotator",
    "name" : "BRENDA",
    "description" : "",
    "url" : "http://www.brenda-enzymes.org",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Gene", "lcsb.mapviewer.model.map.species.Rna" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "TAIR_LOCUS",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "UNIPROT",
      "order" : 1,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "BRENDA",
      "order" : 2,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.EnsemblAnnotator",
    "name" : "Ensembl",
    "description" : "",
    "url" : "https://www.ensembl.org/",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Rna", "lcsb.mapviewer.model.map.species.Gene" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "ENSEMBL",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "ENTREZ",
      "order" : 1,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "HGNC",
      "order" : 2,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "HGNC_SYMBOL",
      "order" : 3,
      "type" : "OUTPUT"
    }, {
      "field" : "FULL_NAME",
      "annotation_type" : null,
      "order" : 4,
      "type" : "OUTPUT"
    }, {
      "field" : "SYMBOL",
      "annotation_type" : null,
      "order" : 5,
      "type" : "OUTPUT"
    }, {
      "field" : "SYNONYMS",
      "annotation_type" : null,
      "order" : 6,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.CazyAnnotator",
    "name" : "CAZy",
    "description" : "",
    "url" : "http://commonchemistry.org",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Gene", "lcsb.mapviewer.model.map.species.Rna" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "TAIR_LOCUS",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "UNIPROT",
      "order" : 1,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "CAZY",
      "order" : 2,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.ReconAnnotator",
    "name" : "Recon annotator",
    "description" : "",
    "url" : "https://www.vmh.life/",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Chemical", "lcsb.mapviewer.model.map.reaction.Reaction" ],
    "parameters" : [ {
      "field" : "ABBREVIATION",
      "annotation_type" : "VMH_METABOLITE",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : "NAME",
      "annotation_type" : "VMH_METABOLITE",
      "order" : 1,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "VMH_METABOLITE",
      "order" : 2,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "EC",
      "order" : 3,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "CHEBI",
      "order" : 4,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "KEGG_COMPOUND",
      "order" : 5,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "KEGG_REACTION",
      "order" : 6,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "KEGG_ORTHOLOGY",
      "order" : 7,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "PUBCHEM",
      "order" : 8,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "HMDB",
      "order" : 9,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "INCHI",
      "order" : 10,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "INCHIKEY",
      "order" : 11,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "COG",
      "order" : 12,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "VMH_METABOLITE",
      "order" : 13,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "VMH_REACTION",
      "order" : 14,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "CHEMSPIDER",
      "order" : 15,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "WIKIPEDIA",
      "order" : 16,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "CAS",
      "order" : 17,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "CHEMBL_COMPOUND",
      "order" : 18,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "MESH_2012",
      "order" : 19,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "RHEA",
      "order" : 20,
      "type" : "OUTPUT"
    }, {
      "field" : "ABBREVIATION",
      "annotation_type" : null,
      "order" : 21,
      "type" : "OUTPUT"
    }, {
      "field" : "DESCRIPTION",
      "annotation_type" : null,
      "order" : 22,
      "type" : "OUTPUT"
    }, {
      "field" : "FORMULA",
      "annotation_type" : null,
      "order" : 23,
      "type" : "OUTPUT"
    }, {
      "field" : "MCS",
      "annotation_type" : null,
      "order" : 24,
      "type" : "OUTPUT"
    }, {
      "field" : "CHARGE",
      "annotation_type" : null,
      "order" : 25,
      "type" : "OUTPUT"
    }, {
      "field" : "SUBSYSTEM",
      "annotation_type" : null,
      "order" : 26,
      "type" : "OUTPUT"
    }, {
      "field" : "SYNONYMS",
      "annotation_type" : null,
      "order" : 27,
      "type" : "OUTPUT"
    }, {
      "field" : "SMILE",
      "annotation_type" : null,
      "order" : 28,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.HgncAnnotator",
    "name" : "HGNC",
    "description" : "",
    "url" : "http://www.genenames.org",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Rna", "lcsb.mapviewer.model.map.species.Gene" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "HGNC_SYMBOL",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "HGNC",
      "order" : 1,
      "type" : "INPUT"
    }, {
      "field" : "NAME",
      "annotation_type" : "HGNC_SYMBOL",
      "order" : 2,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "ENSEMBL",
      "order" : 3,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "ENTREZ",
      "order" : 4,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "HGNC",
      "order" : 5,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "HGNC_SYMBOL",
      "order" : 6,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "REFSEQ",
      "order" : 7,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "UNIPROT",
      "order" : 8,
      "type" : "OUTPUT"
    }, {
      "field" : "SYMBOL",
      "annotation_type" : null,
      "order" : 9,
      "type" : "OUTPUT"
    }, {
      "field" : "SYNONYMS",
      "annotation_type" : null,
      "order" : 10,
      "type" : "OUTPUT"
    }, {
      "field" : "NAME",
      "annotation_type" : null,
      "order" : 11,
      "type" : "OUTPUT"
    }, {
      "field" : "FULL_NAME",
      "annotation_type" : null,
      "order" : 12,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.UniprotAnnotator",
    "name" : "Uniprot",
    "description" : "",
    "url" : "http://www.uniprot.org/",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Gene", "lcsb.mapviewer.model.map.species.Rna" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "UNIPROT",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : "NAME",
      "annotation_type" : "UNIPROT",
      "order" : 1,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "HGNC_SYMBOL",
      "order" : 2,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "UNIPROT",
      "order" : 3,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "EC",
      "order" : 4,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "STRING",
      "order" : 5,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "ENTREZ",
      "order" : 6,
      "type" : "OUTPUT"
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.KeggAnnotator",
    "name" : "KEGG",
    "description" : "Annotations extracted from KEGG ENZYME Database based on species EC numbers. Annotation include relevant publications and homologous genes for given EC numbers.",
    "url" : "https://www.genome.jp/kegg/",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Protein", "lcsb.mapviewer.model.map.species.Gene", "lcsb.mapviewer.model.map.species.Rna" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "TAIR_LOCUS",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "UNIPROT",
      "order" : 1,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "EC",
      "order" : 2,
      "type" : "INPUT"
    }, {
      "field" : null,
      "annotation_type" : "PUBMED",
      "order" : 3,
      "type" : "OUTPUT"
    }, {
      "field" : null,
      "annotation_type" : "TAIR_LOCUS",
      "order" : 4,
      "type" : "OUTPUT"
    }, {
      "type" : "CONFIG",
      "name" : "KEGG_ORGANISM_IDENTIFIER",
      "commonName" : "KEGG organism identifier",
      "inputType" : "java.lang.String",
      "description" : "Space-delimited list of organisms codes for which homologous genes (final GENE section in the KEGG enzyme record) should be imported. Currently only ATH (final Arabidopsis Thaliana) is supported.",
      "value" : "",
      "order" : 5
    } ]
  }, {
    "className" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
    "name" : "Gene Ontology",
    "description" : "",
    "url" : "http://amigo.geneontology.org/amigo",
    "elementClassNames" : [ "lcsb.mapviewer.model.map.species.Phenotype", "lcsb.mapviewer.model.map.compartment.Compartment", "lcsb.mapviewer.model.map.species.Complex" ],
    "parameters" : [ {
      "field" : null,
      "annotation_type" : "GO",
      "order" : 0,
      "type" : "INPUT"
    }, {
      "field" : "FULL_NAME",
      "annotation_type" : null,
      "order" : 1,
      "type" : "OUTPUT"
    }, {
      "field" : "DESCRIPTION",
      "annotation_type" : null,
      "order" : 2,
      "type" : "OUTPUT"
    } ]
  } ],
  "bioEntityFields" : [ {
    "commonName" : "Abbreviation",
    "name" : "ABBREVIATION"
  }, {
    "commonName" : "Charge",
    "name" : "CHARGE"
  }, {
    "commonName" : "Description",
    "name" : "DESCRIPTION"
  }, {
    "commonName" : "Formula",
    "name" : "FORMULA"
  }, {
    "commonName" : "Full name",
    "name" : "FULL_NAME"
  }, {
    "commonName" : "Name",
    "name" : "NAME"
  }, {
    "commonName" : "Mechanical Confidence Score",
    "name" : "MCS"
  }, {
    "commonName" : "Previous Symbols",
    "name" : "PREVIOUS_SYMBOLS"
  }, {
    "commonName" : "Smile",
    "name" : "SMILE"
  }, {
    "commonName" : "Symbol",
    "name" : "SYMBOL"
  }, {
    "commonName" : "Synonyms",
    "name" : "SYNONYMS"
  }, {
    "commonName" : "Subsystem",
    "name" : "SUBSYSTEM"
  } ]
}
```


Title: Rest API Documentation - Files

URL Source: https://ontox.elixir-luxembourg.org/minerva/docs/file.html

Markdown Content:
1\. Create new file in the system
---------------------------------

### 1.1. CURL sample

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/files/' -X POST \
    -d 'filename=test_file&length=999999' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
```

### 1.2. Request Parameters

 
| Parameter | Description |
| --- | --- |
| `filename`
 | original name of the file

 |
| `length`

 | length of the file (in bytes)

 |

### 1.3. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `id`
 | `number`

 | unique id in the system

 |
| `filename`

 | `number`

 | original name of the file

 |
| `length`

 | `number`

 | file length

 |
| `owner`

 | `number`

 | login of the file owner

 |
| `uploadedDataLength`

 | `number`

 | total number of uploaded bytes

 |

### 1.4. Sample Response

```
{
  "id" : 227,
  "filename" : "test_file",
  "length" : 999999,
  "owner" : "admin",
  "uploadedDataLength" : 0
}
```

2\. Upload content of the file
------------------------------

### 2.1. CURL sample

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/files/227:uploadContent' -X POST \
    --data-binary @input_file.txt \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/octet-stream'
```

### 2.2. Request Parameters

 
| Parameter | Description |
| --- | --- |

### 2.3. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `id`
 | `number`

 | unique id in the system

 |
| `filename`

 | `number`

 | original name of the file

 |
| `length`

 | `number`

 | file length

 |
| `owner`

 | `number`

 | login of the file owner

 |
| `uploadedDataLength`

 | `number`

 | total number of uploaded bytes

 |

### 2.4. Sample Response

```
{
  "id" : 227,
  "filename" : "test_file",
  "length" : 999999,
  "owner" : "admin",
  "uploadedDataLength" : 24
}
```

3\. Get info about file
-----------------------

### 3.1. CURL sample

```
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/files/228' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
```

### 3.2. Path Parameters

Table 1. /minerva/api/files/{fileId}  
| Parameter | Description |
| --- | --- |
| `fileId`
 | file id

 |

### 3.3. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `id`
 | `number`

 | unique id in the system

 |
| `filename`

 | `number`

 | original name of the file

 |
| `length`

 | `number`

 | file length

 |
| `owner`

 | `number`

 | login of the file owner

 |
| `uploadedDataLength`

 | `number`

 | total number of uploaded bytes

 |

### 3.4. Sample Response

```
{
  "id" : 228,
  "filename" : "test_file",
  "length" : 11,
  "owner" : "admin",
  "uploadedDataLength" : 11
}
```

Title: Rest API Documentation - Genome

URL Source: https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html

Markdown Content:
Rest API Documentation - Genome
===============

Rest API Documentation - Genome
===============================

minerva  
version 18.2.1 2025-04-24T11:05:57Z

[API-docs](https://ontox.elixir-luxembourg.org/minerva/docs/index.html)  
  
Table of Contents

*   [1\. Get all organism available on remote server that have genome data available](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_get_all_organism_available_on_remote_server_that_have_genome_data_available)
    *   [1.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample)
    *   [1.2. Response Fields](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_response_fields)
    *   [1.3. Sample Response](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_sample_response)
*   [2\. Get all genome types (remote databases) that support given organism.](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_get_all_genome_types_remote_databases_that_support_given_organism)
    *   [2.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_2)
    *   [2.2. Path Parameters](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_path_parameters)
    *   [2.3. Response Fields](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_response_fields_2)
    *   [2.4. Sample Response](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_sample_response_2)
*   [3\. Get all available genome versions for specified organism and genome type](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_get_all_available_genome_versions_for_specified_organism_and_genome_type)
    *   [3.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_3)
    *   [3.2. Path Parameters](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_path_parameters_2)
    *   [3.3. Response Fields](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_response_fields_3)
    *   [3.4. Sample Response](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_sample_response_3)
*   [4\. Get remote url for specified genome, version, and remote database](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_get_remote_url_for_specified_genome_version_and_remote_database)
    *   [4.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_4)
    *   [4.2. Path Parameters](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_path_parameters_3)
    *   [4.3. Response Fields](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_response_fields_4)
    *   [4.4. Sample Response](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_sample_response_4)
*   [5\. Start downloading genome data from remote database to minerva](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_start_downloading_genome_data_from_remote_database_to_minerva)
    *   [5.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_5)
    *   [5.2. Request Parameters](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_request_parameters)
*   [6\. Get information about specific downloaded genome](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_get_information_about_specific_downloaded_genome)
    *   [6.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_6)
    *   [6.2. Path Parameters](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_path_parameters_4)
    *   [6.3. Response Fields](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_response_fields_5)
    *   [6.4. Sample Response](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_sample_response_5)
*   [7\. Get information about all downloaded genomes](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_get_information_about_all_downloaded_genomes)
    *   [7.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_7)
    *   [7.2. Response Fields](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_response_fields_6)
    *   [7.3. Sample Response](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_sample_response_6)
*   [8\. Delete downloaded genome](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_delete_downloaded_genome)
    *   [8.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_8)
    *   [8.2. Path Parameters](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_path_parameters_5)
*   [9\. Add gene mapping](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_add_gene_mapping)
    *   [9.1. Path Parameters](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_path_parameters_6)
    *   [9.2. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_9)
*   [10\. Delete gene mapping](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_delete_gene_mapping)
    *   [10.1. CURL sample](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_curl_sample_10)
    *   [10.2. Path Parameters](https://ontox.elixir-luxembourg.org/minerva/docs/genomics.html#_path_parameters_7)

1\. Get all organism available on remote server that have genome data available
-------------------------------------------------------------------------------

### 1.1. CURL sample

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_organisms/curl-request.adoc\[\]

### 1.2. Response Fields

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_organisms/response-fields.adoc\[\]

### 1.3. Sample Response

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_organisms/response-body.adoc\[\]

2\. Get all genome types (remote databases) that support given organism.
------------------------------------------------------------------------

### 2.1. CURL sample

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_genome\_types/curl-request.adoc\[\]

### 2.2. Path Parameters

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_genome\_types/path-parameters.adoc\[\]

### 2.3. Response Fields

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_genome\_types/response-fields.adoc\[\]

### 2.4. Sample Response

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_genome\_types/response-body.adoc\[\]

3\. Get all available genome versions for specified organism and genome type
----------------------------------------------------------------------------

### 3.1. CURL sample

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_genome\_versions/curl-request.adoc\[\]

### 3.2. Path Parameters

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_genome\_versions/path-parameters.adoc\[\]

### 3.3. Response Fields

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_genome\_versions/response-fields.adoc\[\]

### 3.4. Sample Response

Unresolved directive in genomics.adoc - include::../../../target/generated-snippets/genomics/get\_genome\_versions/response-body.adoc\[\]

4\. Get remote url for specified genome, version, and remote database
---------------------------------------------------------------------

### 4.1. CURL sample

```bash
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/genomics/taxonomies/9606/genomeTypes/UCSC/versions/hg38:getAvailableRemoteUrls' -X GET
```

### 4.2. Path Parameters

Table 1. /minerva/api/genomics/taxonomies/{taxonomyId}/genomeTypes/{genomeType}/versions/{version}:getAvailableRemoteUrls  
| Parameter | Description |
| --- | --- |
| `taxonomyId`
 | organism taxonomy id

 |
| `genomeType`

 | genome type, acceptable values: UCSC

 |
| `version`

 | genome version

 |

### 4.3. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `[]`
 | `array`

 | list of urls

 |
| `[].url`

 | `string`

 | url

 |

### 4.4. Sample Response

```
[ {
  "url" : "https://hgdownload.soe.ucsc.edu//goldenPath/hg38/bigZips/hg38.2bit"
} ]
```

5\. Start downloading genome data from remote database to minerva
-----------------------------------------------------------------

### 5.1. CURL sample

```bash
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/genomics/' -X POST \
    -d 'organismId=1570291&type=UCSC&version=eboVir3&url=http%3A%2F%2Fminerva-dev.lcsb.uni.lu%2FeboVir3.2bit' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
```

### 5.2. Request Parameters

 
| Parameter | Description |
| --- | --- |
| `organismId`
 | organism taxonomy id

 |
| `type`

 | genome type, acceptable values: UCSC

 |
| `version`

 | genome version

 |
| `url`

 | url address from where the file should be downloaded

 |

6\. Get information about specific downloaded genome
----------------------------------------------------

### 6.1. CURL sample

```bash
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/genomics/taxonomies/1570291/genomeTypes/UCSC/versions/eboVir3/' -X GET
```

### 6.2. Path Parameters

Table 2. /minerva/api/genomics/taxonomies/{taxonomyId}/genomeTypes/{genomeType}/versions/{version}/  
| Parameter | Description |
| --- | --- |
| `taxonomyId`
 | organism taxonomy id

 |
| `genomeType`

 | genome type, acceptable values: UCSC

 |
| `version`

 | genome version

 |

### 6.3. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `downloadProgress`
 | `double`

 | download progress (0-100%)

 |
| `geneMapping`

 | `Array`

 | list of available gene mappings for given genome

 |
| `geneMapping[].name`

 | `String`

 | name of the gene mapping

 |
| `geneMapping[].sourceUrl`

 | `String`

 | source url of the gene mapping

 |
| `geneMapping[].localUrl`

 | `String`

 | url with local copy of the mapping

 |
| `geneMapping[].downloadProgress`

 | `Number`

 | download progress

 |
| `geneMapping[].idObject`

 | `Number`

 | id of the gene mapping

 |
| `idObject`

 | `Number`

 | unique id of genome in minerva

 |
| `localUrl`

 | `String`

 | url on minerva where local copy of genome can be accessed

 |
| `organism`

 | `Object`

 | organism identifier

 |
| `organism.resource`

 | `String`

 | organism identifier

 |
| `organism.type`

 | `String`

 | organism identifier type (usually TAXONOMY)

 |
| `sourceUrl`

 | `String`

 | genome source url

 |
| `type`

 | `String`

 | type of genome (database from which it was downloaded)

 |
| `version`

 | `String`

 | genome version

 |

### 6.4. Sample Response

```
{
  "organism" : {
    "link" : null,
    "type" : "TAXONOMY",
    "resource" : "1570291",
    "id" : 1188,
    "annotatorClassName" : ""
  },
  "version" : "eboVir3",
  "type" : "UCSC",
  "downloadProgress" : 100.0,
  "sourceUrl" : "ftp://hgdownload.cse.ucsc.edu/goldenPath/eboVir3/bigZips/eboVir3.2bit",
  "localUrl" : "ftp://hgdownload.cse.ucsc.edu/goldenPath/eboVir3/bigZips/eboVir3.2bit",
  "idObject" : 15,
  "geneMapping" : [ {
    "downloadProgress" : 0.0,
    "localUrl" : "https://minerva-dev.lcsb.uni.lu/tmp/refGene.bb",
    "sourceUrl" : "https://minerva-dev.lcsb.uni.lu/tmp/refGene.bb",
    "name" : "custom-gene-mapping",
    "idObject" : 17
  } ]
}
```

7\. Get information about all downloaded genomes
------------------------------------------------

### 7.1. CURL sample

```bash
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/genomics/' -X GET
```

### 7.2. Response Fields

  
| Path | Type | Description |
| --- | --- | --- |
| `[]`
 | `array`

 | list of downloaded genomes

 |
| `[].downloadProgress`

 | `double`

 | download progress (0-100%)

 |
| `[].geneMapping`

 | `Array`

 | list of available gene mappings for given genome

 |
| `[].geneMapping[].name`

 | `String`

 | name of the gene mapping

 |
| `[].geneMapping[].sourceUrl`

 | `String`

 | source url of the gene mapping

 |
| `[].geneMapping[].localUrl`

 | `String`

 | url with local copy of the mapping

 |
| `[].geneMapping[].downloadProgress`

 | `Number`

 | download progress

 |
| `[].geneMapping[].idObject`

 | `Number`

 | id of the gene mapping

 |
| `[].idObject`

 | `Number`

 | unique id of genome in minerva

 |
| `[].localUrl`

 | `String`

 | url on minerva where local copy of genome can be accessed

 |
| `[].organism`

 | `Object`

 | organism identifier

 |
| `[].organism.resource`

 | `String`

 | organism identifier

 |
| `[].organism.type`

 | `String`

 | organism identifier type (usually TAXONOMY)

 |
| `[].sourceUrl`

 | `String`

 | genome source url

 |
| `[].type`

 | `String`

 | type of genome (database from which it was downloaded)

 |
| `[].version`

 | `String`

 | genome version

 |

### 7.3. Sample Response

```
[ {
  "organism" : {
    "link" : null,
    "type" : "TAXONOMY",
    "resource" : "1570291",
    "id" : 1186,
    "annotatorClassName" : ""
  },
  "version" : "eboVir3",
  "type" : "UCSC",
  "downloadProgress" : 100.0,
  "sourceUrl" : "ftp://hgdownload.cse.ucsc.edu/goldenPath/eboVir3/bigZips/eboVir3.2bit",
  "localUrl" : "ftp://hgdownload.cse.ucsc.edu/goldenPath/eboVir3/bigZips/eboVir3.2bit",
  "idObject" : 13,
  "geneMapping" : [ {
    "downloadProgress" : 0.0,
    "localUrl" : "https://minerva-dev.lcsb.uni.lu/tmp/refGene.bb",
    "sourceUrl" : "https://minerva-dev.lcsb.uni.lu/tmp/refGene.bb",
    "name" : "custom-gene-mapping",
    "idObject" : 16
  } ]
} ]
```

8\. Delete downloaded genome
----------------------------

### 8.1. CURL sample

```bash
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/genomics/11/' -X DELETE \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
```

### 8.2. Path Parameters

Table 3. /minerva/api/genomics/{genomeId}/  
| Parameter | Description |
| --- | --- |
| `genomeId`
 | genome id (genomeId is retrieved as idObject described above in 6.3)

 |

9\. Add gene mapping
--------------------

### 9.1. Path Parameters

Table 4. /minerva/api/genomics/{genomeId}/geneMapping/  
| Parameter | Description |
| --- | --- |
| `genomeId`
 | genome id (genomeId is retrieved as idObject described above in 6.3)

 |

### 9.2. CURL sample

```bash
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/genomics/12/geneMapping/' -X POST \
    -d 'name=mappingName&url=https%3A%2F%2Fminerva-dev.lcsb.uni.lu%2Ftmp%2FrefGene.bb' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
```

10\. Delete gene mapping
------------------------

### 10.1. CURL sample

```bash
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/genomics/10/geneMapping/11/' -X DELETE \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
```

### 10.2. Path Parameters

Table 5. /minerva/api/genomics/{genomeId}/geneMapping/{geneMappingId}/  
| Parameter | Description |
| --- | --- |
| `genomeId`
 | genome id (genomeId is retrieved as idObject described above in 6.3)

 |
| `geneMappingId`

 | gene genome mapping id (geneMapping\[\].objectId described in 6.3)

 |

Version 18.2.1 2025-04-24T11:05:57Z  
Last updated 2025-04-11 04:37:57 UTC

Title: Rest API Documentation - Licenses

URL Source: https://ontox.elixir-luxembourg.org/minerva/docs/license.html

Markdown Content:
```
{
  "data" : [ {
    "id" : 1,
    "name" : "CC0 1.0 Universal",
    "content" : "\n<h3><em>Statement of Purpose</em></h3>\n<p>The laws of most jurisdictions throughout the world\nautomatically confer exclusive Copyright and Related Rights\n(defined below) upon the creator and subsequent owner(s) (each\nand all, an \"owner\") of an original work of authorship and/or\na database (each, a \"Work\").</p>\n<p>Certain owners wish to permanently relinquish those rights\nto a Work for the purpose of contributing to a commons of\ncreative, cultural and scientific works (\"Commons\") that the\npublic can reliably and without fear of later claims of\ninfringement build upon, modify, incorporate in other works,\nreuse and redistribute as freely as possible in any form\nwhatsoever and for any purposes, including without limitation\ncommercial purposes. These owners may contribute to the\nCommons to promote the ideal of a free culture and the further\nproduction of creative, cultural and scientific works, or to\ngain reputation or greater distribution for their Work in part\nthrough the use and efforts of others.</p>\n<p>For these and/or other purposes and motivations, and\nwithout any expectation of additional consideration or\ncompensation, the person associating CC0 with a Work (the\n\"Affirmer\"), to the extent that he or she is an owner of\nCopyright and Related Rights in the Work, voluntarily elects\nto apply CC0 to the Work and publicly distribute the Work\nunder its terms, with knowledge of his or her Copyright and\nRelated Rights in the Work and the meaning and intended legal\neffect of CC0 on those rights.</p>\n<p><strong>1. Copyright and Related Rights.</strong>\nA Work made available under CC0 may be protected by\ncopyright and related or neighboring rights (\"Copyright and\nRelated Rights\"). Copyright and Related Rights include, but\nare not limited to, the following:\n</p>\n<ol type=\"i\">\n<li>the right to reproduce, adapt, distribute, perform,\ndisplay, communicate, and translate a Work;</li>\n<li> moral rights retained by the original author(s) and/or\nperformer(s);</li>\n<li>publicity and privacy rights pertaining to a person's\nimage or likeness depicted in a Work;</li>\n<li>rights protecting against unfair competition in regards\nto a Work, subject to the limitations in paragraph 4(a),\nbelow;</li>\n<li>rights protecting the extraction, dissemination, use and\nreuse of data in a Work;</li>\n<li>database rights (such as those arising under Directive\n96/9/EC of the European Parliament and of the Council of 11\nMarch 1996 on the legal protection of databases, and under\nany national implementation thereof, including any amended\nor successor version of such directive); and</li>\n<li>other similar, equivalent or corresponding rights\nthroughout the world based on applicable law or treaty, and\nany national implementations thereof.</li>\n</ol>\n<p><strong>2. Waiver.</strong> To the greatest extent\npermitted by, but not in contravention of, applicable law,\nAffirmer hereby overtly, fully, permanently, irrevocably and\nunconditionally waives, abandons, and surrenders all of\nAffirmer's Copyright and Related Rights and associated claims\nand causes of action, whether now known or unknown (including\nexisting as well as future claims and causes of action), in\nthe Work (i) in all territories worldwide, (ii) for the\nmaximum duration provided by applicable law or treaty\n(including future time extensions), (iii) in any current or\nfuture medium and for any number of copies, and (iv) for any\npurpose whatsoever, including without limitation commercial,\nadvertising or promotional purposes (the \"Waiver\"). Affirmer\nmakes the Waiver for the benefit of each member of the public\nat large and to the detriment of Affirmer's heirs and\nsuccessors, fully intending that such Waiver shall not be\nsubject to revocation, rescission, cancellation, termination,\nor any other legal or equitable action to disrupt the quiet\nenjoyment of the Work by the public as contemplated by\nAffirmer's express Statement of Purpose.\n</p>\n<p><strong>3. Public License Fallback.</strong> Should any\npart of the Waiver for any reason be judged legally invalid or\nineffective under applicable law, then the Waiver shall be\npreserved to the maximum extent permitted taking into account\nAffirmer's express Statement of Purpose. In addition, to the\nextent the Waiver is so judged Affirmer hereby grants to each\naffected person a royalty-free, non transferable, non\nsublicensable, non exclusive, irrevocable and unconditional\nlicense to exercise Affirmer's Copyright and Related Rights\nin the Work (i) in all territories worldwide, (ii) for the\nmaximum duration provided by applicable law or treaty\n(including future time extensions), (iii) in any current or\nfuture medium and for any number of copies, and (iv) for any\npurpose whatsoever, including without limitation commercial,\nadvertising or promotional purposes (the \"License\"). The\nLicense shall be deemed effective as of the date CC0 was\napplied by Affirmer to the Work. Should any part of the\nLicense for any reason be judged legally invalid or\nineffective under applicable law, such partial invalidity or\nineffectiveness shall not invalidate the remainder of the\nLicense, and in such case Affirmer hereby affirms that he or\nshe will not (i) exercise any of his or her remaining\nCopyright and Related Rights in the Work or (ii) assert any\nassociated claims and causes of action with respect to the\nWork, in either case contrary to Affirmer's express Statement\nof Purpose.</p>\n<p><strong>4. Limitations and Disclaimers.</strong></p>\n<ol type=\"a\">\n<li>No trademark or patent rights held by Affirmer are\nwaived, abandoned, surrendered, licensed or otherwise\naffected by this document.</li>\n<li>Affirmer offers the Work as-is and makes no\nrepresentations or warranties of any kind concerning the\nWork, express, implied, statutory or otherwise, including\nwithout limitation warranties of title, merchantability,\nfitness for a particular purpose, non infringement, or the\nabsence of latent or other defects, accuracy, or the present\nor absence of errors, whether or not discoverable, all to\nthe greatest extent permissible under applicable law.</li>\n<li>Affirmer disclaims responsibility for clearing rights of\nother persons that may apply to the Work or any use thereof,\nincluding without limitation any person's Copyright and\nRelated Rights in the Work. Further, Affirmer disclaims\nresponsibility for obtaining any necessary consents,\npermissions or other rights required for any use of the\nWork.</li>\n<li>Affirmer understands and acknowledges that Creative\nCommons is not a party to this document and has no duty or\nobligation with respect to this CC0 or use of the Work.</li>\n</ol>\n",
    "url" : "https://creativecommons.org/publicdomain/zero/1.0/"
  }, {
    "id" : 2,
    "name" : "Creative Commons Attribution 4.0 International Public License",
    "content" : "\n<h3>Creative Commons Attribution 4.0 International Public License</h3>\n<p>By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution 4.0 International Public License (\"Public License\"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.</p>\n<p id=\"s1\"><strong>Section 1 – Definitions.</strong></p>\n<ol type=\"a\">\n<li id=\"s1a\"><strong>Adapted Material</strong> means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.</li>\n<li id=\"s1b\"><strong>Adapter's License</strong> means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.</li>\n<li id=\"s1c\"><strong>Copyright and Similar Rights</strong> means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section <a href=\"#s2b\">2(b)(1)-(2)</a> are not Copyright and Similar Rights.</li>\n<li id=\"s1d\"><strong>Effective Technological Measures</strong> means those measures that, in the absence of proper authority, may not\nbe circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar\ninternational agreements.</li>\n<li id=\"s1e\"><strong>Exceptions and Limitations</strong> means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.</li>\n<li id=\"s1f\"><strong>Licensed Material</strong> means the artistic or literary work, database, or other material to which the Licensor applied this Public License.</li>\n<li id=\"s1g\"><strong>Licensed Rights</strong> means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.</li>\n<li id=\"s1h\"><strong>Licensor</strong> means the individual(s) or entity(ies) granting rights under this Public License.</li>\n<li id=\"s1i\"><strong>Share</strong> means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.</li>\n<li id=\"s1j\"><strong>Sui Generis Database Rights</strong> means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.</li>\n<li id=\"s1k\"><strong>You</strong> means the individual or entity exercising the Licensed Rights under this Public License. <strong>Your</strong> has a corresponding meaning.</li>\n</ol>\n<p id=\"s2\"><strong>Section 2 – Scope.</strong></p>\n<ol type=\"a\">\n<li id=\"s2a\"><strong>License grant</strong>.\n<ol>\n<li id=\"s2a1\">Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:\n<ol type=\"A\">\n<li id=\"s2a1A\">reproduce and Share the Licensed Material, in whole or in part; and</li>\n<li id=\"s2a1B\">produce, reproduce, and Share Adapted Material.</li>\n</ol>\n</li><li id=\"s2a2\"><span style=\"text-decoration: underline;\">Exceptions and Limitations</span>. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.</li>\n<li id=\"s2a3\"><span style=\"text-decoration: underline;\">Term</span>. The term of this Public License is specified in Section <a href=\"#s6a\">6(a)</a>.</li>\n<li id=\"s2a4\"><span style=\"text-decoration: underline;\">Media and formats; technical modifications allowed</span>. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section <a href=\"#s2a4\">2(a)(4)</a> never produces Adapted Material.</li>\n<li id=\"s2a5\"><span style=\"text-decoration: underline;\">Downstream recipients</span>.\n<div class=\"para\">\n<ol type=\"A\">\n<li id=\"s2a5A\"><span style=\"text-decoration: underline;\">Offer from the Licensor – Licensed Material</span>. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.</li>\n<li id=\"s2a5B\"><span style=\"text-decoration: underline;\">No downstream restrictions</span>. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.</li>\n</ol>\n</div>\n</li><li id=\"s2a6\"><span style=\"text-decoration: underline;\">No endorsement</span>. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section <a href=\"#s3a1Ai\">3(a)(1)(A)(i)</a>.</li>\n</ol>\n</li><li id=\"s2b\"><p><strong>Other rights</strong>.</p>\n<ol>\n<li id=\"s2b1\">Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.</li>\n<li id=\"s2b2\">Patent and trademark rights are not licensed under this Public License.</li>\n<li id=\"s2b3\">To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s3\"><strong>Section 3 – License Conditions.</strong></p>\n<p>Your exercise of the Licensed Rights is expressly made subject to the following conditions.</p>\n<ol type=\"a\">\n<li id=\"s3a\"><p><strong>Attribution</strong>.</p>\n<ol>\n<li id=\"s3a1\"><p>If You Share the Licensed Material (including in modified form), You must:</p>\n<ol type=\"A\">\n<li id=\"s3a1A\">retain the following if it is supplied by the Licensor with the Licensed Material:\n<ol type=\"i\">\n<li id=\"s3a1Ai\">identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);</li>\n<li id=\"s3a1Aii\">a copyright notice;</li>\n<li id=\"s3a1Aiii\">a notice that refers to this Public License; </li>\n<li id=\"s3a1Aiv\">a notice that refers to the disclaimer of warranties;</li>\n<li id=\"s3a1Av\">a URI or hyperlink to the Licensed Material to the extent reasonably practicable;</li>\n</ol>\n</li><li id=\"s3a1B\">indicate if You modified the Licensed Material and retain an indication of any previous modifications; and</li>\n<li id=\"s3a1C\">indicate the Licensed Material is licensed under this Public License,\nand include the text of, or the URI or hyperlink to, this Public\nLicense.</li>\n</ol>\n</li>\n<li id=\"s3a2\">You may satisfy the conditions in Section <a href=\"#s3a1\">3(a)(1)</a> in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.</li>\n<li id=\"s3a3\">If requested by the Licensor, You must remove any of the information required by Section <a href=\"#s3a1A\">3(a)(1)(A)</a> to the extent reasonably practicable.</li>\n<li id=\"s3a4\">If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s4\"><strong>Section 4 – Sui Generis Database Rights.</strong></p>\n<p>Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:</p>\n<ol type=\"a\">\n<li id=\"s4a\">for the avoidance of doubt, Section <a href=\"#s2a1\">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database;</li>\n<li id=\"s4b\">if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and</li>\n<li id=\"s4c\">You must comply with the conditions in Section <a href=\"#s3a\">3(a)</a> if You Share all or a substantial portion of the contents of the database.</li>\n</ol>\nFor the avoidance of doubt, this Section\n<a href=\"#s4\">4</a>\n supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.\n<p id=\"s5\"><strong>Section 5 – Disclaimer of Warranties and Limitation of Liability.</strong></p>\n<ol style=\"font-weight: bold;\" type=\"a\">\n<li id=\"s5a\"><strong>Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.</strong></li>\n<li id=\"s5b\"><strong>To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.</strong></li>\n</ol>\n<ol start=\"3\" type=\"a\">\n<li id=\"s5c\">The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.</li>\n</ol>\n<p id=\"s6\"><strong>Section 6 – Term and Termination.</strong></p>\n<ol type=\"a\">\n<li id=\"s6a\">This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.</li>\n<li id=\"s6b\">\n<p>Where Your right to use the Licensed Material has terminated under Section <a href=\"#s6a\">6(a)</a>, it reinstates:</p>\n<ol>\n<li id=\"s6b1\">automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or</li>\n<li id=\"s6b2\">upon express reinstatement by the Licensor.</li>\n</ol>\nFor the avoidance of doubt, this Section <a href=\"#s6b\">6(b)</a> does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.</li>\n<li id=\"s6c\">For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.</li>\n<li id=\"s6d\">Sections <a href=\"#s1\">1</a>, <a href=\"#s5\">5</a>, <a href=\"#s6\">6</a>, <a href=\"#s7\">7</a>, and <a href=\"#s8\">8</a> survive termination of this Public License.</li>\n</ol>\n<p id=\"s7\"><strong>Section 7 – Other Terms and Conditions.</strong></p>\n<ol type=\"a\">\n<li id=\"s7a\">The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.</li>\n<li id=\"s7b\">Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.</li>\n</ol>\n<p id=\"s8\"><strong>Section 8 – Interpretation.</strong></p>\n<ol type=\"a\">\n<li id=\"s8a\">For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.</li>\n<li id=\"s8b\">To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.</li>\n<li id=\"s8c\">No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.</li>\n<li id=\"s8d\">Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.</li>\n</ol>",
    "url" : "https://creativecommons.org/licenses/by/4.0/"
  }, {
    "id" : 3,
    "name" : "Creative Commons Attribution-ShareAlike 4.0 International Public License",
    "content" : "\n<h3>Creative Commons Attribution-ShareAlike 4.0 International Public License</h3>\n<p>By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-ShareAlike 4.0 International Public License (\"Public License\"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.</p>\n<p id=\"s1\"><strong>Section 1 – Definitions.</strong></p>\n<ol type=\"a\">\n<li id=\"s1a\"><strong>Adapted Material</strong> means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.</li>\n<li id=\"s1b\"><strong>Adapter's License</strong> means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.</li>\n<li id=\"s1c\"><strong>BY-SA Compatible License</strong> means a license listed at <a href=\"//creativecommons.org/compatiblelicenses\"> creativecommons.org/compatiblelicenses</a>, approved by Creative Commons as essentially the equivalent of this Public License.</li>\n<li id=\"s1d\"><strong>Copyright and Similar Rights</strong> means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section <a href=\"#s2b\">2(b)(1)-(2)</a> are not Copyright and Similar Rights.</li>\n<li id=\"s1e\"><strong>Effective Technological Measures</strong> means those measures that, in the absence of proper authority, may not\nbe circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar\ninternational agreements.</li>\n<li id=\"s1f\"><strong>Exceptions and Limitations</strong> means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.</li>\n<li id=\"s1g\"><strong>License Elements</strong> means the license attributes listed in the name of a Creative Commons Public License. The License Elements of this Public License are Attribution and ShareAlike.</li>\n<li id=\"s1h\"><strong>Licensed Material</strong> means the artistic or literary work, database, or other material to which the Licensor applied this Public License.</li>\n<li id=\"s1i\"><strong>Licensed Rights</strong> means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.</li>\n<li id=\"s1j\"><strong>Licensor</strong> means the individual(s) or entity(ies) granting rights under this Public License.</li>\n<li id=\"s1k\"><strong>Share</strong> means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.</li>\n<li id=\"s1l\"><strong>Sui Generis Database Rights</strong> means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.</li>\n<li id=\"s1m\"><strong>You</strong> means the individual or entity exercising the Licensed Rights under this Public License. <strong>Your</strong> has a corresponding meaning.</li>\n</ol>\n<p id=\"s2\"><strong>Section 2 – Scope.</strong></p>\n<ol type=\"a\">\n<li id=\"s2a\"><strong>License grant</strong>.\n<ol>\n<li id=\"s2a1\">Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:\n<ol type=\"A\">\n<li id=\"s2a1A\">reproduce and Share the Licensed Material, in whole or in part; and</li>\n<li id=\"s2a1B\">produce, reproduce, and Share Adapted Material.</li>\n</ol>\n</li><li id=\"s2a2\"><span style=\"text-decoration: underline;\">Exceptions and Limitations</span>. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.</li>\n<li id=\"s2a3\"><span style=\"text-decoration: underline;\">Term</span>. The term of this Public License is specified in Section <a href=\"#s6a\">6(a)</a>.</li>\n<li id=\"s2a4\"><span style=\"text-decoration: underline;\">Media and formats; technical modifications allowed</span>. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section <a href=\"#s2a4\">2(a)(4)</a> never produces Adapted Material.</li>\n<li id=\"s2a5\"><span style=\"text-decoration: underline;\">Downstream recipients</span>.\n<div class=\"para\">\n<ol type=\"A\">\n<li id=\"s2a5A\"><span style=\"text-decoration: underline;\">Offer from the Licensor – Licensed Material</span>. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.</li>\n<li id=\"s2a5B\"><span style=\"text-decoration: underline;\">Additional offer from the Licensor – Adapted Material</span>. Every recipient of Adapted Material from You automatically receives an offer from the Licensor to exercise the Licensed Rights in the Adapted Material under the conditions of the Adapter’s License You apply.</li>\n<li id=\"s2a5C\"><span style=\"text-decoration: underline;\">No downstream restrictions</span>. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.</li>\n</ol>\n</div>\n</li><li id=\"s2a6\"><span style=\"text-decoration: underline;\">No endorsement</span>. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section <a href=\"#s3a1Ai\">3(a)(1)(A)(i)</a>.</li>\n</ol>\n</li><li id=\"s2b\"><p><strong>Other rights</strong>.</p>\n<ol>\n<li id=\"s2b1\">Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.</li>\n<li id=\"s2b2\">Patent and trademark rights are not licensed under this Public License.</li>\n<li id=\"s2b3\">To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s3\"><strong>Section 3 – License Conditions.</strong></p>\n<p>Your exercise of the Licensed Rights is expressly made subject to the following conditions.</p>\n<ol type=\"a\">\n<li id=\"s3a\"><p><strong>Attribution</strong>.</p>\n<ol>\n<li id=\"s3a1\"><p>If You Share the Licensed Material (including in modified form), You must:</p>\n<ol type=\"A\">\n<li id=\"s3a1A\">retain the following if it is supplied by the Licensor with the Licensed Material:\n<ol type=\"i\">\n<li id=\"s3a1Ai\">identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);</li>\n<li id=\"s3a1Aii\">a copyright notice;</li>\n<li id=\"s3a1Aiii\">a notice that refers to this Public License; </li>\n<li id=\"s3a1Aiv\">a notice that refers to the disclaimer of warranties;</li>\n<li id=\"s3a1Av\">a URI or hyperlink to the Licensed Material to the extent reasonably practicable;</li>\n</ol>\n</li><li id=\"s3a1B\">indicate if You modified the Licensed Material and retain an indication of any previous modifications; and</li>\n<li id=\"s3a1C\">indicate the Licensed Material is licensed under this Public License,\nand include the text of, or the URI or hyperlink to, this Public\nLicense.</li>\n</ol>\n</li>\n<li id=\"s3a2\">You may satisfy the conditions in Section <a href=\"#s3a1\">3(a)(1)</a> in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.</li>\n<li id=\"s3a3\">If requested by the Licensor, You must remove any of the information required by Section <a href=\"#s3a1A\">3(a)(1)(A)</a> to the extent reasonably practicable.</li>\n</ol>\n</li>\n<li id=\"s3b\"><strong>ShareAlike</strong>.\n<p>In addition to the conditions in Section <a href=\"#s3a\">3(a)</a>, if You Share Adapted Material You produce, the following conditions also apply.</p>\n<ol>\n<li id=\"s3b1\">The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-SA Compatible License.</li>\n<li id=\"s3b2\">You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. You may satisfy this condition in any reasonable manner based on the medium, means, and context in which You Share Adapted Material.</li>\n<li id=\"s3b3\">You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, Adapted Material that restrict exercise of the rights granted under the Adapter's License You apply.</li>\n</ol>\n</li>\n</ol>\n<p>Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:</p>\n<ol type=\"a\">\n<li id=\"s4a\">for the avoidance of doubt, Section <a href=\"#s2a1\">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database;</li>\n<li id=\"s4b\">if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material, including for purposes of Section <a href=\"#s3b\">3(b)</a>; and</li>\n<li id=\"s4c\">You must comply with the conditions in Section <a href=\"#s3a\">3(a)</a> if You Share all or a substantial portion of the contents of the database.</li>\n</ol>\nFor the avoidance of doubt, this Section \n<a href=\"#s4\">4</a>\n supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.\n<p id=\"s5\"><strong>Section 5 – Disclaimer of Warranties and Limitation of Liability.</strong></p>\n<ol style=\"font-weight: bold;\" type=\"a\">\n<li id=\"s5a\"><strong>Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.</strong></li>\n<li id=\"s5b\"><strong>To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.</strong></li>\n</ol>\n<ol start=\"3\" type=\"a\">\n<li id=\"s5c\">The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.</li>\n</ol>\n<p id=\"s6\"><strong>Section 6 – Term and Termination.</strong></p>\n<ol type=\"a\">\n<li id=\"s6a\">This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.</li>\n<li id=\"s6b\">\n<p>Where Your right to use the Licensed Material has terminated under Section <a href=\"#s6a\">6(a)</a>, it reinstates:</p>\n<ol>\n<li id=\"s6b1\">automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or</li>\n<li id=\"s6b2\">upon express reinstatement by the Licensor.</li>\n</ol>\nFor the avoidance of doubt, this Section <a href=\"#s6b\">6(b)</a> does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.</li>\n<li id=\"s6c\">For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.</li>\n<li id=\"s6d\">Sections <a href=\"#s1\">1</a>, <a href=\"#s5\">5</a>, <a href=\"#s6\">6</a>, <a href=\"#s7\">7</a>, and <a href=\"#s8\">8</a> survive termination of this Public License.</li>\n</ol>\n<p id=\"s7\"><strong>Section 7 – Other Terms and Conditions.</strong></p>\n<ol type=\"a\">\n<li id=\"s7a\">The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.</li>\n<li id=\"s7b\">Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.</li>\n</ol>\n<p id=\"s8\"><strong>Section 8 – Interpretation.</strong></p>\n<ol type=\"a\">\n<li id=\"s8a\">For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.</li>\n<li id=\"s8b\">To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.</li>\n<li id=\"s8c\">No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.</li>\n<li id=\"s8d\">Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.</li>\n</ol>\n",
    "url" : "https://creativecommons.org/licenses/by-sa/4.0/"
  }, {
    "id" : 4,
    "name" : "Creative Commons Attribution-NonCommercial 4.0 International",
    "content" : "\n<h3>Creative Commons Attribution-NonCommercial 4.0 International Public License</h3>\n<p>By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial 4.0 International Public License (\"Public License\"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.</p>\n<p id=\"s1\"><strong>Section 1 – Definitions.</strong></p>\n<ol type=\"a\">\n<li id=\"s1a\"><strong>Adapted Material</strong> means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.</li>\n<li id=\"s1b\"><strong>Adapter's License</strong> means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.</li>\n<li id=\"s1c\"><strong>Copyright and Similar Rights</strong> means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section <a href=\"#s2b\">2(b)(1)-(2)</a> are not Copyright and Similar Rights.</li>\n<li id=\"s1d\"><strong>Effective Technological Measures</strong> means those measures that, in the absence of proper authority, may not\nbe circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar\ninternational agreements.</li>\n<li id=\"s1e\"><strong>Exceptions and Limitations</strong> means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.</li>\n<li id=\"s1f\"><strong>Licensed Material</strong> means the artistic or literary work, database, or other material to which the Licensor applied this Public License.</li>\n<li id=\"s1g\"><strong>Licensed Rights</strong> means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.</li>\n<li id=\"s1h\"><strong>Licensor</strong> means the individual(s) or entity(ies) granting rights under this Public License.</li>\n<li id=\"s1i\"><strong>NonCommercial</strong> means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.</li>\n<li id=\"s1j\"><strong>Share</strong> means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.</li>\n<li id=\"s1k\"><strong>Sui Generis Database Rights</strong> means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.</li>\n<li id=\"s1l\"><strong>You</strong> means the individual or entity exercising the Licensed Rights under this Public License. <strong>Your</strong> has a corresponding meaning.</li>\n</ol>\n<p id=\"s2\"><strong>Section 2 – Scope.</strong></p>\n<ol type=\"a\">\n<li id=\"s2a\"><strong>License grant</strong>.\n<ol>\n<li id=\"s2a1\">Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:\n<ol type=\"A\">\n<li id=\"s2a1A\">reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and</li>\n<li id=\"s2a1B\">produce, reproduce, and Share Adapted Material for NonCommercial purposes only.</li>\n</ol>\n</li><li id=\"s2a2\"><span style=\"text-decoration: underline;\">Exceptions and Limitations</span>. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.</li>\n<li id=\"s2a3\"><span style=\"text-decoration: underline;\">Term</span>. The term of this Public License is specified in Section <a href=\"#s6a\">6(a)</a>.</li>\n<li id=\"s2a4\"><span style=\"text-decoration: underline;\">Media and formats; technical modifications allowed</span>. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section <a href=\"#s2a4\">2(a)(4)</a> never produces Adapted Material.</li>\n<li id=\"s2a5\"><span style=\"text-decoration: underline;\">Downstream recipients</span>.\n<div class=\"para\">\n<ol type=\"A\">\n<li id=\"s2a5A\"><span style=\"text-decoration: underline;\">Offer from the Licensor – Licensed Material</span>. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.</li>\n<li id=\"s2a5B\"><span style=\"text-decoration: underline;\">No downstream restrictions</span>. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.</li>\n</ol>\n</div>\n</li><li id=\"s2a6\"><span style=\"text-decoration: underline;\">No endorsement</span>. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section <a href=\"#s3a1Ai\">3(a)(1)(A)(i)</a>.</li>\n</ol>\n</li><li id=\"s2b\"><p><strong>Other rights</strong>.</p>\n<ol>\n<li id=\"s2b1\">Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.</li>\n<li id=\"s2b2\">Patent and trademark rights are not licensed under this Public License.</li>\n<li id=\"s2b3\">To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s3\"><strong>Section 3 – License Conditions.</strong></p>\n<p>Your exercise of the Licensed Rights is expressly made subject to the following conditions.</p>\n<ol type=\"a\">\n<li id=\"s3a\"><p><strong>Attribution</strong>.</p>\n<ol>\n<li id=\"s3a1\"><p>If You Share the Licensed Material (including in modified form), You must:</p>\n<ol type=\"A\">\n<li id=\"s3a1A\">retain the following if it is supplied by the Licensor with the Licensed Material:\n<ol type=\"i\">\n<li id=\"s3a1Ai\">identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);</li>\n<li id=\"s3a1Aii\">a copyright notice;</li>\n<li id=\"s3a1Aiii\">a notice that refers to this Public License; </li>\n<li id=\"s3a1Aiv\">a notice that refers to the disclaimer of warranties;</li>\n<li id=\"s3a1Av\">a URI or hyperlink to the Licensed Material to the extent reasonably practicable;</li>\n</ol>\n</li><li id=\"s3a1B\">indicate if You modified the Licensed Material and retain an indication of any previous modifications; and</li>\n<li id=\"s3a1C\">indicate the Licensed Material is licensed under this Public License,\nand include the text of, or the URI or hyperlink to, this Public\nLicense.</li>\n</ol>\n</li>\n<li id=\"s3a2\">You may satisfy the conditions in Section <a href=\"#s3a1\">3(a)(1)</a> in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.</li>\n<li id=\"s3a3\">If requested by the Licensor, You must remove any of the information required by Section <a href=\"#s3a1A\">3(a)(1)(A)</a> to the extent reasonably practicable.</li>\n<li id=\"s3a4\">If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s4\"><strong>Section 4 – Sui Generis Database Rights.</strong></p>\n<p>Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:</p>\n<ol type=\"a\">\n<li id=\"s4a\">for the avoidance of doubt, Section <a href=\"#s2a1\">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only;</li>\n<li id=\"s4b\">if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and</li>\n<li id=\"s4c\">You must comply with the conditions in Section <a href=\"#s3a\">3(a)</a> if You Share all or a substantial portion of the contents of the database.</li>\n</ol>\nFor the avoidance of doubt, this Section \n<a href=\"#s4\">4</a>\n supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.\n<p id=\"s5\"><strong>Section 5 – Disclaimer of Warranties and Limitation of Liability.</strong></p>\n<ol style=\"font-weight: bold;\" type=\"a\">\n<li id=\"s5a\"><strong>Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.</strong></li>\n<li id=\"s5b\"><strong>To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.</strong></li>\n</ol>\n<ol start=\"3\" type=\"a\">\n<li id=\"s5c\">The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.</li>\n</ol>\n<p id=\"s6\"><strong>Section 6 – Term and Termination.</strong></p>\n<ol type=\"a\">\n<li id=\"s6a\">This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.</li>\n<li id=\"s6b\">\n<p>Where Your right to use the Licensed Material has terminated under Section <a href=\"#s6a\">6(a)</a>, it reinstates:</p>\n<ol>\n<li id=\"s6b1\">automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or</li>\n<li id=\"s6b2\">upon express reinstatement by the Licensor.</li>\n</ol>\nFor the avoidance of doubt, this Section <a href=\"#s6b\">6(b)</a> does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.</li>\n<li id=\"s6c\">For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.</li>\n<li id=\"s6d\">Sections <a href=\"#s1\">1</a>, <a href=\"#s5\">5</a>, <a href=\"#s6\">6</a>, <a href=\"#s7\">7</a>, and <a href=\"#s8\">8</a> survive termination of this Public License.</li>\n</ol>\n<p id=\"s7\"><strong>Section 7 – Other Terms and Conditions.</strong></p>\n<ol type=\"a\">\n<li id=\"s7a\">The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.</li>\n<li id=\"s7b\">Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.</li>\n</ol>\n<p id=\"s8\"><strong>Section 8 – Interpretation.</strong></p>\n<ol type=\"a\">\n<li id=\"s8a\">For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.</li>\n<li id=\"s8b\">To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.</li>\n<li id=\"s8c\">No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.</li>\n<li id=\"s8d\">Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.</li>\n</ol>\n",
    "url" : "https://creativecommons.org/licenses/by-nc/4.0/"
  }, {
    "id" : 5,
    "name" : "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License",
    "content" : "\n<h3>Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License</h3>\n<p>By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (\"Public License\"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.</p>\n<p id=\"s1\"><strong>Section 1 – Definitions.</strong></p>\n<ol type=\"a\">\n<li id=\"s1a\"><strong>Adapted Material</strong> means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.</li>\n<li id=\"s1b\"><strong>Adapter's License</strong> means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.</li>\n<li id=\"s1c\"><strong>BY-NC-SA Compatible License</strong> means a license listed at <a href=\"//creativecommons.org/compatiblelicenses\"> creativecommons.org/compatiblelicenses</a>, approved by Creative Commons as essentially the equivalent of this Public License.</li>\n<li id=\"s1d\"><strong>Copyright and Similar Rights</strong> means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section <a href=\"#s2b\">2(b)(1)-(2)</a> are not Copyright and Similar Rights.</li>\n<li id=\"s1e\"><strong>Effective Technological Measures</strong> means those measures that, in the absence of proper authority, may not\nbe circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar\ninternational agreements.</li>\n<li id=\"s1f\"><strong>Exceptions and Limitations</strong> means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.</li>\n<li id=\"s1g\"><strong>License Elements</strong> means the license attributes listed in the name of a Creative Commons Public License. The License Elements of this Public License are Attribution, NonCommercial, and ShareAlike.</li>\n<li id=\"s1h\"><strong>Licensed Material</strong> means the artistic or literary work, database, or other material to which the Licensor applied this Public License.</li>\n<li id=\"s1i\"><strong>Licensed Rights</strong> means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.</li>\n<li id=\"s1j\"><strong>Licensor</strong> means the individual(s) or entity(ies) granting rights under this Public License.</li>\n<li id=\"s1k\"><strong>NonCommercial</strong> means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.</li>\n<li id=\"s1l\"><strong>Share</strong> means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.</li>\n<li id=\"s1m\"><strong>Sui Generis Database Rights</strong> means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.</li>\n<li id=\"s1n\"><strong>You</strong> means the individual or entity exercising the Licensed Rights under this Public License. <strong>Your</strong> has a corresponding meaning.</li>\n</ol>\n<p id=\"s2\"><strong>Section 2 – Scope.</strong></p>\n<ol type=\"a\">\n<li id=\"s2a\"><strong>License grant</strong>.\n<ol>\n<li id=\"s2a1\">Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:\n<ol type=\"A\">\n<li id=\"s2a1A\">reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and</li>\n<li id=\"s2a1B\">produce, reproduce, and Share Adapted Material for NonCommercial purposes only.</li>\n</ol>\n</li><li id=\"s2a2\"><span style=\"text-decoration: underline;\">Exceptions and Limitations</span>. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.</li>\n<li id=\"s2a3\"><span style=\"text-decoration: underline;\">Term</span>. The term of this Public License is specified in Section <a href=\"#s6a\">6(a)</a>.</li>\n<li id=\"s2a4\"><span style=\"text-decoration: underline;\">Media and formats; technical modifications allowed</span>. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section <a href=\"#s2a4\">2(a)(4)</a> never produces Adapted Material.</li>\n<li id=\"s2a5\"><span style=\"text-decoration: underline;\">Downstream recipients</span>.\n<div class=\"para\">\n<ol type=\"A\">\n<li id=\"s2a5A\"><span style=\"text-decoration: underline;\">Offer from the Licensor – Licensed Material</span>. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.</li>\n<li id=\"s2a5B\"><span style=\"text-decoration: underline;\">Additional offer from the Licensor – Adapted Material</span>. Every recipient of Adapted Material from You automatically receives an offer from the Licensor to exercise the Licensed Rights in the Adapted Material under the conditions of the Adapter’s License You apply.</li>\n<li id=\"s2a5C\"><span style=\"text-decoration: underline;\">No downstream restrictions</span>. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.</li>\n</ol>\n</div>\n</li><li id=\"s2a6\"><span style=\"text-decoration: underline;\">No endorsement</span>. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section <a href=\"#s3a1Ai\">3(a)(1)(A)(i)</a>.</li>\n</ol>\n</li><li id=\"s2b\"><p><strong>Other rights</strong>.</p>\n<ol>\n<li id=\"s2b1\">Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.</li>\n<li id=\"s2b2\">Patent and trademark rights are not licensed under this Public License.</li>\n<li id=\"s2b3\">To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s3\"><strong>Section 3 – License Conditions.</strong></p>\n<p>Your exercise of the Licensed Rights is expressly made subject to the following conditions.</p>\n<ol type=\"a\">\n<li id=\"s3a\"><p><strong>Attribution</strong>.</p>\n<ol>\n<li id=\"s3a1\"><p>If You Share the Licensed Material (including in modified form), You must:</p>\n<ol type=\"A\">\n<li id=\"s3a1A\">retain the following if it is supplied by the Licensor with the Licensed Material:\n<ol type=\"i\">\n<li id=\"s3a1Ai\">identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);</li>\n<li id=\"s3a1Aii\">a copyright notice;</li>\n<li id=\"s3a1Aiii\">a notice that refers to this Public License; </li>\n<li id=\"s3a1Aiv\">a notice that refers to the disclaimer of warranties;</li>\n<li id=\"s3a1Av\">a URI or hyperlink to the Licensed Material to the extent reasonably practicable;</li>\n</ol>\n</li><li id=\"s3a1B\">indicate if You modified the Licensed Material and retain an indication of any previous modifications; and</li>\n<li id=\"s3a1C\">indicate the Licensed Material is licensed under this Public License,\nand include the text of, or the URI or hyperlink to, this Public\nLicense.</li>\n</ol>\n</li>\n<li id=\"s3a2\">You may satisfy the conditions in Section <a href=\"#s3a1\">3(a)(1)</a> in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.</li>\n<li id=\"s3a3\">If requested by the Licensor, You must remove any of the information required by Section <a href=\"#s3a1A\">3(a)(1)(A)</a> to the extent reasonably practicable.</li>\n</ol>\n</li>\n<li id=\"s3b\"><strong>ShareAlike</strong>.\n<p>In addition to the conditions in Section <a href=\"#s3a\">3(a)</a>, if You Share Adapted Material You produce, the following conditions also apply.</p>\n<ol>\n<li id=\"s3b1\">The Adapter’s License You apply must be a Creative Commons license with the same License Elements, this version or later, or a BY-NC-SA Compatible License.</li>\n<li id=\"s3b2\">You must include the text of, or the URI or hyperlink to, the Adapter's License You apply. You may satisfy this condition in any reasonable manner based on the medium, means, and context in which You Share Adapted Material.</li>\n<li id=\"s3b3\">You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, Adapted Material that restrict exercise of the rights granted under the Adapter's License You apply.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s4\"><strong>Section 4 – Sui Generis Database Rights.</strong></p>\n<p>Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:</p>\n<ol type=\"a\">\n<li id=\"s4a\">for the avoidance of doubt, Section <a href=\"#s2a1\">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only;</li>\n<li id=\"s4b\">if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material, including for purposes of Section <a href=\"#s3b\">3(b)</a>; and</li>\n<li id=\"s4c\">You must comply with the conditions in Section <a href=\"#s3a\">3(a)</a> if You Share all or a substantial portion of the contents of the database.</li>\n</ol>\nFor the avoidance of doubt, this Section \n<a href=\"#s4\">4</a>\n supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.\n<p id=\"s5\"><strong>Section 5 – Disclaimer of Warranties and Limitation of Liability.</strong></p>\n<ol style=\"font-weight: bold;\" type=\"a\">\n<li id=\"s5a\"><strong>Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.</strong></li>\n<li id=\"s5b\"><strong>To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.</strong></li>\n</ol>\n<ol start=\"3\" type=\"a\">\n<li id=\"s5c\">The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.</li>\n</ol>\n<p id=\"s6\"><strong>Section 6 – Term and Termination.</strong></p>\n<ol type=\"a\">\n<li id=\"s6a\">This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.</li>\n<li id=\"s6b\">\n<p>Where Your right to use the Licensed Material has terminated under Section <a href=\"#s6a\">6(a)</a>, it reinstates:</p>\n<ol>\n<li id=\"s6b1\">automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or</li>\n<li id=\"s6b2\">upon express reinstatement by the Licensor.</li>\n</ol>\nFor the avoidance of doubt, this Section <a href=\"#s6b\">6(b)</a> does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.</li>\n<li id=\"s6c\">For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.</li>\n<li id=\"s6d\">Sections <a href=\"#s1\">1</a>, <a href=\"#s5\">5</a>, <a href=\"#s6\">6</a>, <a href=\"#s7\">7</a>, and <a href=\"#s8\">8</a> survive termination of this Public License.</li>\n</ol>\n<p id=\"s7\"><strong>Section 7 – Other Terms and Conditions.</strong></p>\n<ol type=\"a\">\n<li id=\"s7a\">The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.</li>\n<li id=\"s7b\">Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.</li>\n</ol>\n<p id=\"s8\"><strong>Section 8 – Interpretation.</strong></p>\n<ol type=\"a\">\n<li id=\"s8a\">For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.</li>\n<li id=\"s8b\">To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.</li>\n<li id=\"s8c\">No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.</li>\n<li id=\"s8d\">Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.</li>\n</ol>\n",
    "url" : "https://creativecommons.org/licenses/by-nc-sa/4.0/"
  }, {
    "id" : 6,
    "name" : "Creative Commons Attribution-NoDerivatives 4.0 International Public License",
    "content" : "\n<h3>Creative Commons Attribution-NoDerivatives 4.0 International Public License</h3>\n<p>By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NoDerivatives 4.0 International Public License (\"Public License\"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.</p>\n<p id=\"s1\"><strong>Section 1 – Definitions.</strong></p>\n<ol type=\"a\">\n<li id=\"s1a\"><strong>Adapted Material</strong> means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.</li>\n<li id=\"s1b\"><strong>Copyright and Similar Rights</strong> means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section <a href=\"#s2b\">2(b)(1)-(2)</a> are not Copyright and Similar Rights.</li>\n<li id=\"s1c\"><strong>Effective Technological Measures</strong> means those measures that, in the absence of proper authority, may not\nbe circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar\ninternational agreements.</li>\n<li id=\"s1d\"><strong>Exceptions and Limitations</strong> means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.</li>\n<li id=\"s1e\"><strong>Licensed Material</strong> means the artistic or literary work, database, or other material to which the Licensor applied this Public License.</li>\n<li id=\"s1f\"><strong>Licensed Rights</strong> means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.</li>\n<li id=\"s1g\"><strong>Licensor</strong> means the individual(s) or entity(ies) granting rights under this Public License.</li>\n<li id=\"s1h\"><strong>Share</strong> means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.</li>\n<li id=\"s1i\"><strong>Sui Generis Database Rights</strong> means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.</li>\n<li id=\"s1j\"><strong>You</strong> means the individual or entity exercising the Licensed Rights under this Public License. <strong>Your</strong> has a corresponding meaning.</li>\n</ol>\n<p id=\"s2\"><strong>Section 2 – Scope.</strong></p>\n<ol type=\"a\">\n<li id=\"s2a\"><strong>License grant</strong>.\n<ol>\n<li id=\"s2a1\">Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:\n<ol type=\"A\">\n<li id=\"s2a1A\">reproduce and Share the Licensed Material, in whole or in part; and</li>\n<li id=\"s2a1B\">produce and reproduce, but not Share, Adapted Material.</li>\n</ol>\n</li><li id=\"s2a2\"><span style=\"text-decoration: underline;\">Exceptions and Limitations</span>. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.</li>\n<li id=\"s2a3\"><span style=\"text-decoration: underline;\">Term</span>. The term of this Public License is specified in Section <a href=\"#s6a\">6(a)</a>.</li>\n<li id=\"s2a4\"><span style=\"text-decoration: underline;\">Media and formats; technical modifications allowed</span>. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section <a href=\"#s2a4\">2(a)(4)</a> never produces Adapted Material.</li>\n<li id=\"s2a5\"><span style=\"text-decoration: underline;\">Downstream recipients</span>.\n<div class=\"para\">\n<ol type=\"A\">\n<li id=\"s2a5A\"><span style=\"text-decoration: underline;\">Offer from the Licensor – Licensed Material</span>. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.</li>\n<li id=\"s2a5B\"><span style=\"text-decoration: underline;\">No downstream restrictions</span>. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.</li>\n</ol>\n</div>\n</li><li id=\"s2a6\"><span style=\"text-decoration: underline;\">No endorsement</span>. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section <a href=\"#s3a1Ai\">3(a)(1)(A)(i)</a>.</li>\n</ol>\n</li><li id=\"s2b\"><p><strong>Other rights</strong>.</p>\n<ol>\n<li id=\"s2b1\">Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.</li>\n<li id=\"s2b2\">Patent and trademark rights are not licensed under this Public License.</li>\n<li id=\"s2b3\">To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s3\"><strong>Section 3 – License Conditions.</strong></p>\n<p>Your exercise of the Licensed Rights is expressly made subject to the following conditions.</p>\n<ol type=\"a\">\n<li id=\"s3a\"><p><strong>Attribution</strong>.</p>\n<ol>\n<li id=\"s3a1\"><p>If You Share the Licensed Material, You must:</p>\n<ol type=\"A\">\n<li id=\"s3a1A\">retain the following if it is supplied by the Licensor with the Licensed Material:\n<ol type=\"i\">\n<li id=\"s3a1Ai\">identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);</li>\n<li id=\"s3a1Aii\">a copyright notice;</li>\n<li id=\"s3a1Aiii\">a notice that refers to this Public License; </li>\n<li id=\"s3a1Aiv\">a notice that refers to the disclaimer of warranties;</li>\n<li id=\"s3a1Av\">a URI or hyperlink to the Licensed Material to the extent reasonably practicable;</li>\n</ol>\n</li><li id=\"s3a1B\">indicate if You modified the Licensed Material and retain an indication of any previous modifications; and</li>\n<li id=\"s3a1C\">indicate the Licensed Material is licensed under this Public License,\nand include the text of, or the URI or hyperlink to, this Public\nLicense.</li>\n</ol>\nFor the avoidance of doubt, You do not have permission under this Public License to Share Adapted Material.\n</li>\n<li id=\"s3a2\">You may satisfy the conditions in Section <a href=\"#s3a1\">3(a)(1)</a> in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.</li>\n<li id=\"s3a3\">If requested by the Licensor, You must remove any of the information required by Section <a href=\"#s3a1A\">3(a)(1)(A)</a> to the extent reasonably practicable.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s4\"><strong>Section 4 – Sui Generis Database Rights.</strong></p>\n<p>Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:</p>\n<ol type=\"a\">\n<li id=\"s4a\">for the avoidance of doubt, Section <a href=\"#s2a1\">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database, provided You do not Share Adapted Material;</li>\n<li id=\"s4b\">if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and</li>\n<li id=\"s4c\">You must comply with the conditions in Section <a href=\"#s3a\">3(a)</a> if You Share all or a substantial portion of the contents of the database.</li>\n</ol>\nFor the avoidance of doubt, this Section\n<a href=\"#s4\">4</a>\n supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.\n<p id=\"s5\"><strong>Section 5 – Disclaimer of Warranties and Limitation of Liability.</strong></p>\n<ol style=\"font-weight: bold;\" type=\"a\">\n<li id=\"s5a\"><strong>Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.</strong></li>\n<li id=\"s5b\"><strong>To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.</strong></li>\n</ol>\n<ol start=\"3\" type=\"a\">\n<li id=\"s5c\">The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.</li>\n</ol>\n<p id=\"s6\"><strong>Section 6 – Term and Termination.</strong></p>\n<ol type=\"a\">\n<li id=\"s6a\">This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.</li>\n<li id=\"s6b\">\n<p>Where Your right to use the Licensed Material has terminated under Section <a href=\"#s6a\">6(a)</a>, it reinstates:</p>\n<ol>\n<li id=\"s6b1\">automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or</li>\n<li id=\"s6b2\">upon express reinstatement by the Licensor.</li>\n</ol>\nFor the avoidance of doubt, this Section <a href=\"#s6b\">6(b)</a> does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.</li>\n<li id=\"s6c\">For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.</li>\n<li id=\"s6d\">Sections <a href=\"#s1\">1</a>, <a href=\"#s5\">5</a>, <a href=\"#s6\">6</a>, <a href=\"#s7\">7</a>, and <a href=\"#s8\">8</a> survive termination of this Public License.</li>\n</ol>\n<p id=\"s7\"><strong>Section 7 – Other Terms and Conditions.</strong></p>\n<ol type=\"a\">\n<li id=\"s7a\">The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.</li>\n<li id=\"s7b\">Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.</li>\n</ol>\n<p id=\"s8\"><strong>Section 8 – Interpretation.</strong></p>\n<ol type=\"a\">\n<li id=\"s8a\">For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.</li>\n<li id=\"s8b\">To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.</li>\n<li id=\"s8c\">No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.</li>\n<li id=\"s8d\">Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.</li>\n</ol>\n",
    "url" : "https://creativecommons.org/licenses/by-nd/4.0/"
  }, {
    "id" : 7,
    "name" : "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License",
    "content" : "\n<h3>Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License</h3>\n<p>By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License (\"Public License\"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.</p>\n<p id=\"s1\"><strong>Section 1 – Definitions.</strong></p>\n<ol type=\"a\">\n<li id=\"s1a\"><strong>Adapted Material</strong> means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.</li>\n<li id=\"s1b\"><strong>Copyright and Similar Rights</strong> means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section <a href=\"#s2b\">2(b)(1)-(2)</a> are not Copyright and Similar Rights.</li>\n<li id=\"s1c\"><strong>Effective Technological Measures</strong> means those measures that, in the absence of proper authority, may not\nbe circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar\ninternational agreements.</li>\n<li id=\"s1d\"><strong>Exceptions and Limitations</strong> means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.</li>\n<li id=\"s1e\"><strong>Licensed Material</strong> means the artistic or literary work, database, or other material to which the Licensor applied this Public License.</li>\n<li id=\"s1f\"><strong>Licensed Rights</strong> means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.</li>\n<li id=\"s1g\"><strong>Licensor</strong> means the individual(s) or entity(ies) granting rights under this Public License.</li>\n<li id=\"s1h\"><strong>NonCommercial</strong> means not primarily intended for or directed towards commercial advantage or monetary compensation. For purposes of this Public License, the exchange of the Licensed Material for other material subject to Copyright and Similar Rights by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange.</li>\n<li id=\"s1i\"><strong>Share</strong> means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.</li>\n<li id=\"s1j\"><strong>Sui Generis Database Rights</strong> means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.</li>\n<li id=\"s1k\"><strong>You</strong> means the individual or entity exercising the Licensed Rights under this Public License. <strong>Your</strong> has a corresponding meaning.</li>\n</ol>\n<p id=\"s2\"><strong>Section 2 – Scope.</strong></p>\n<ol type=\"a\">\n<li id=\"s2a\"><strong>License grant</strong>.\n<ol>\n<li id=\"s2a1\">Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:\n<ol type=\"A\">\n<li id=\"s2a1A\">reproduce and Share the Licensed Material, in whole or in part, for NonCommercial purposes only; and</li>\n<li id=\"s2a1B\">produce and reproduce, but not Share, Adapted Material for NonCommercial purposes only.</li>\n</ol>\n</li><li id=\"s2a2\"><span style=\"text-decoration: underline;\">Exceptions and Limitations</span>. For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.</li>\n<li id=\"s2a3\"><span style=\"text-decoration: underline;\">Term</span>. The term of this Public License is specified in Section <a href=\"#s6a\">6(a)</a>.</li>\n<li id=\"s2a4\"><span style=\"text-decoration: underline;\">Media and formats; technical modifications allowed</span>. The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section <a href=\"#s2a4\">2(a)(4)</a> never produces Adapted Material.</li>\n<li id=\"s2a5\"><span style=\"text-decoration: underline;\">Downstream recipients</span>.\n<div class=\"para\">\n<ol type=\"A\">\n<li id=\"s2a5A\"><span style=\"text-decoration: underline;\">Offer from the Licensor – Licensed Material</span>. Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.</li>\n<li id=\"s2a5B\"><span style=\"text-decoration: underline;\">No downstream restrictions</span>. You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.</li>\n</ol>\n</div>\n</li><li id=\"s2a6\"><span style=\"text-decoration: underline;\">No endorsement</span>. Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section <a href=\"#s3a1Ai\">3(a)(1)(A)(i)</a>.</li>\n</ol>\n</li><li id=\"s2b\"><p><strong>Other rights</strong>.</p>\n<ol>\n<li id=\"s2b1\">Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.</li>\n<li id=\"s2b2\">Patent and trademark rights are not licensed under this Public License.</li>\n<li id=\"s2b3\">To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties, including when the Licensed Material is used other than for NonCommercial purposes.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s3\"><strong>Section 3 – License Conditions.</strong></p>\n<p>Your exercise of the Licensed Rights is expressly made subject to the following conditions.</p>\n<ol type=\"a\">\n<li id=\"s3a\"><p><strong>Attribution</strong>.</p>\n<ol>\n<li id=\"s3a1\"><p>If You Share the Licensed Material, You must:</p>\n<ol type=\"A\">\n<li id=\"s3a1A\">retain the following if it is supplied by the Licensor with the Licensed Material:\n<ol type=\"i\">\n<li id=\"s3a1Ai\">identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);</li>\n<li id=\"s3a1Aii\">a copyright notice;</li>\n<li id=\"s3a1Aiii\">a notice that refers to this Public License; </li>\n<li id=\"s3a1Aiv\">a notice that refers to the disclaimer of warranties;</li>\n<li id=\"s3a1Av\">a URI or hyperlink to the Licensed Material to the extent reasonably practicable;</li>\n</ol>\n</li><li id=\"s3a1B\">indicate if You modified the Licensed Material and retain an indication of any previous modifications; and</li>\n<li id=\"s3a1C\">indicate the Licensed Material is licensed under this Public License,\nand include the text of, or the URI or hyperlink to, this Public\nLicense.</li>\n</ol>\nFor the avoidance of doubt, You do not have permission under this Public License to Share Adapted Material.\n</li>\n<li id=\"s3a2\">You may satisfy the conditions in Section <a href=\"#s3a1\">3(a)(1)</a> in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.</li>\n<li id=\"s3a3\">If requested by the Licensor, You must remove any of the information required by Section <a href=\"#s3a1A\">3(a)(1)(A)</a> to the extent reasonably practicable.</li>\n</ol>\n</li>\n</ol>\n<p id=\"s4\"><strong>Section 4 – Sui Generis Database Rights.</strong></p>\n<p>Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:</p>\n<ol type=\"a\">\n<li id=\"s4a\">for the avoidance of doubt, Section <a href=\"#s2a1\">2(a)(1)</a> grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database for NonCommercial purposes only and provided You do not Share Adapted Material;</li>\n<li id=\"s4b\">if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and</li>\n<li id=\"s4c\">You must comply with the conditions in Section <a href=\"#s3a\">3(a)</a> if You Share all or a substantial portion of the contents of the database.</li>\n</ol>\nFor the avoidance of doubt, this Section \n<a href=\"#s4\">4</a>\n supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.\n<p id=\"s5\"><strong>Section 5 – Disclaimer of Warranties and Limitation of Liability.</strong></p>\n<ol style=\"font-weight: bold;\" type=\"a\">\n<li id=\"s5a\"><strong>Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.</strong></li>\n<li id=\"s5b\"><strong>To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.</strong></li>\n</ol>\n<ol start=\"3\" type=\"a\">\n<li id=\"s5c\">The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.</li>\n</ol>\n<p id=\"s6\"><strong>Section 6 – Term and Termination.</strong></p>\n<ol type=\"a\">\n<li id=\"s6a\">This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.</li>\n<li id=\"s6b\">\n<p>Where Your right to use the Licensed Material has terminated under Section <a href=\"#s6a\">6(a)</a>, it reinstates:</p>\n<ol>\n<li id=\"s6b1\">automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or</li>\n<li id=\"s6b2\">upon express reinstatement by the Licensor.</li>\n</ol>\nFor the avoidance of doubt, this Section <a href=\"#s6b\">6(b)</a> does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.</li>\n<li id=\"s6c\">For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.</li>\n<li id=\"s6d\">Sections <a href=\"#s1\">1</a>, <a href=\"#s5\">5</a>, <a href=\"#s6\">6</a>, <a href=\"#s7\">7</a>, and <a href=\"#s8\">8</a> survive termination of this Public License.</li>\n</ol>\n<p id=\"s7\"><strong>Section 7 – Other Terms and Conditions.</strong></p>\n<ol type=\"a\">\n<li id=\"s7a\">The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.</li>\n<li id=\"s7b\">Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.</li>\n</ol>\n<p id=\"s8\"><strong>Section 8 – Interpretation.</strong></p>\n<ol type=\"a\">\n<li id=\"s8a\">For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.</li>\n<li id=\"s8b\">To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.</li>\n<li id=\"s8c\">No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.</li>\n<li id=\"s8d\">Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.</li>\n</ol>\n",
    "url" : "https://creativecommons.org/licenses/by-nc-nd/4.0/"
  } ],
  "totalSize" : 1,
  "filteredSize" : 0,
  "length" : 20,
  "page" : 0
}
```

Title: Rest API Documentation - Mesh

URL Source: https://ontox.elixir-luxembourg.org/minerva/docs/mesh.html

Markdown Content:
```
{
  "name" : "Parkinson Disease",
  "id" : "D010300",
  "description" : "A progressive, degenerative neurologic disease characterized by a TREMOR that is maximal at rest, retropulsion (i.e. a tendency to fall backwards), rigidity, stooped posture, slowness of voluntary movements, and a masklike facial expression. Pathologic features include loss of melanin containing neurons in the substantia nigra and other pigmented nuclei of the brainstem. LEWY BODIES are present in the substantia nigra and locus coeruleus but may also be found in a related condition (LEWY BODY DISEASE, DIFFUSE) characterized by dementia in combination with varying degrees of parkinsonism. (Adams et al., Principles of Neurology, 6th ed, p1059, pp1067-75)",
  "synonyms" : [ "Parkinson's Disease, Idiopathic", "Primary Parkinsonism", "Idiopathic Parkinson's Disease", "Paralysis Agitans", "Parkinsonism, Primary", "Parkinson's Disease", "Lewy Body Parkinson Disease", "Parkinson's Disease, Lewy Body", "Parkinson Disease, Idiopathic", "Idiopathic Parkinson Disease", "Lewy Body Parkinson's Disease" ]
}
```

Title: Rest API Documentation - Projects

URL Source: https://ontox.elixir-luxembourg.org/minerva/docs/project_data.html

Markdown Content:
```
{
  "elementAnnotations" : {
    "_3DMET" : 0,
    "ABS" : 0,
    "ACEVIEW_WORM" : 0,
    "AFFYMETRIX_PROBESET" : 0,
    "AFTOL" : 0,
    "ALLERGOME" : 0,
    "AMOEBADB" : 0,
    "ANATOMICAL_THERAPEUTIC_CHEMICAL" : 0,
    "ANATOMICAL_THERAPEUTIC_CHEMICAL_VETINARY" : 0,
    "ANIMAL_DIVERSITY_WEB" : 0,
    "ANIMAL_GENOME_CATTLE_QTL" : 0,
    "ANIMAL_GENOME_CHICKEN_QTL" : 0,
    "ANIMAL_GENOME_PIG_QTL" : 0,
    "ANIMAL_GENOME_SHEEP_QTL" : 0,
    "ANIMAL_TFDB_FAMILY" : 0,
    "ANTIBIOTIC_RESISTANCE_GENES_DATABASE" : 0,
    "ANTIBODY_REGISTRY" : 0,
    "ANTWEB" : 0,
    "APD" : 0,
    "APHIDBASE_TRANSCRIPT" : 0,
    "ARACHNOSERVER" : 0,
    "ARRAYEXPRESS" : 0,
    "ARRAYEXPRESS_PLATFORM" : 0,
    "ARXIV" : 0,
    "ASAP" : 0,
    "ASPGD_LOCUS" : 0,
    "ASPGD_PROTEIN" : 0,
    "ATCC" : 0,
    "AUTDB" : 0,
    "BACMAP_BIOGRAPHY" : 0,
    "BACMAP_MAP" : 0,
    "BDGP_EST" : 0,
    "BDGP_INSERTION_DB" : 0,
    "BEETLEBASE" : 0,
    "BGEE_FAMILY" : 0,
    "BGEE_GENE" : 0,
    "BGEE_ORGAN" : 0,
    "BGEE_STAGE" : 0,
    "BiGG_COMPARTMENT" : 0,
    "BiGG_METABOLITE" : 0,
    "BiGG_REACTIONS" : 0,
    "BINDINGDB" : 0,
    "BIOCARTA_PATHWAY" : 0,
    "BIOCATALOGUE" : 0,
    "BIOCYC" : 0,
    "BIOGRID" : 0,
    "BIOKC" : 0,
    "BIOMODELS_DATABASE" : 0,
    "BIONUMBERS" : 0,
    "BIOPORTAL" : 0,
    "BIOPROJECT" : 0,
    "BIOSAMPLE" : 0,
    "BIOSYSTEMS" : 0,
    "BITTERDB_COMPOUND" : 0,
    "BITTERDB_RECEPTOR" : 0,
    "BOLD_TAXONOMY" : 0,
    "BROAD_FUNGAL_GENOME_INITIATIVE" : 0,
    "BRENDA" : 0,
    "BRENDA_TISSUE_ONTOLOGY" : 0,
    "BUGBASE_EXPT" : 0,
    "BUGBASE_PROTOCOL" : 0,
    "BYKDB" : 0,
    "CANADIAN_DRUG_PRODUCT_DATABASE" : 0,
    "CANDIDA_GENOME_DATABASE" : 0,
    "CAPS_DB" : 0,
    "CAS" : 0,
    "CATH_DOMAIN" : 0,
    "CATH_SUPERFAMILY" : 0,
    "CAZY" : 0,
    "CCDS" : 0,
    "CELL_CYCLE_ONTOLOGY" : 0,
    "CELL_IMAGE_LIBRARY" : 0,
    "CELL_SIGNALING_TECHNOLOGY_PATHWAYS" : 0,
    "CELL_SIGNALING_TECHNOLOGY_ANTIBODY" : 0,
    "CELL_TYPE_ONTOLOGY" : 0,
    "CGSC_STRAIN" : 0,
    "CHARPROT" : 0,
    "CHEBI" : 1,
    "CHEMDB" : 0,
    "CHEM_ID_PLUS" : 0,
    "CHEMSPIDER" : 0,
    "CHEMBL_COMPOUND" : 0,
    "CHEMBL_TARGET" : 0,
    "CLDB" : 0,
    "CLINICAL_TRIALS_GOV" : 0,
    "CLINVAR_RECORD" : 0,
    "COG" : 0,
    "COMBINE_SPECIFICATIONS" : 0,
    "COMPLEX_PORTAL" : 0,
    "COMPULYEAST" : 0,
    "CONSERVED_DOMAIN_DATABASE" : 0,
    "CONOSERVER" : 0,
    "CORIELL_CELL_REPOSITORIES" : 0,
    "CORUM" : 0,
    "CPC" : 0,
    "CRYPTODB" : 0,
    "CSA" : 0,
    "CTD_GENE" : 0,
    "CTD_DISEASE" : 0,
    "CUTDB" : 0,
    "CUBE_DB" : 0,
    "DAILYMED" : 0,
    "DARC" : 0,
    "DATABASE_OF_INTERACTING_PROTEINS" : 0,
    "DATABASE_OF_QUANTITATIVE_CELLULAR_SIGNALING_MODEL" : 0,
    "DATABASE_OF_QUANTITATIVE_CELLULAR_SIGNALING_PATHWAY" : 0,
    "DATF" : 0,
    "DBD" : 0,
    "DBEST" : 0,
    "DBG2_INTRONS" : 0,
    "DBPROBE" : 0,
    "DB_SNP" : 0,
    "DEGRADOME_DATABASE" : 0,
    "DEPOD" : 0,
    "DICTYBASE_EST" : 0,
    "DICTYBASE_GENE" : 0,
    "DISPROT" : 0,
    "DOI" : 0,
    "DOMMINO" : 0,
    "DOOR" : 0,
    "DPV" : 0,
    "DRAGONDB_ALLELE" : 0,
    "DRAGONDB_DNA" : 0,
    "DRAGONDB_LOCUS" : 0,
    "DRAGONDB_PROTEIN" : 0,
    "DRSC" : 0,
    "DRUGBANK" : 0,
    "DRUGBANK_TARGET_V4" : 0,
    "EC" : 0,
    "ECHOBASE" : 0,
    "ECO" : 0,
    "ECOGENE" : 0,
    "ECOLIWIKI" : 0,
    "EDAM_ONTOLOGY" : 0,
    "EGGNOG" : 0,
    "ELM" : 0,
    "ENA" : 0,
    "ENSEMBL" : 0,
    "ENSEMBL_BACTERIA" : 0,
    "ENSEMBL_FUNGI" : 0,
    "ENSEMBL_METAZOA" : 0,
    "ENSEMBL_PLANTS" : 0,
    "ENSEMBL_PROTISTS" : 0,
    "ENTREZ" : 0,
    "ENVIPATH" : 0,
    "EPD" : 0,
    "EU_CLINICAL_TRIALS" : 0,
    "EXAC_GENE" : 0,
    "EXAC_TRANSCRIPT" : 0,
    "EXAC_VARIANT" : 0,
    "EXPERIMENTAL_FACTOR_ONTOLOGY" : 0,
    "EUROPEAN_GENOME_PHENOME_ARCHIVE_DATASET" : 0,
    "EUROPEAN_GENOME_PHENOME_ARCHIVE_STUDY" : 0,
    "FMA" : 0,
    "FOODB_COMPOUND" : 0,
    "F_SNP" : 0,
    "FUNCBASE_FLY" : 0,
    "FUNCBASE_HUMAN" : 0,
    "FUNCBASE_MOUSE" : 0,
    "FUNCBASE_YEAST" : 0,
    "FUNGIDB" : 0,
    "FLYBASE" : 0,
    "GABI" : 0,
    "GENATLAS" : 0,
    "GENECARDS" : 0,
    "GENE_DB" : 0,
    "GENEFARM" : 0,
    "GENETREE" : 0,
    "GENE_WIKI" : 0,
    "GENPEPT" : 0,
    "GENOME_PROPERTIES" : 0,
    "GENOMIC_DATA_COMMONS_DATA_PORTAL" : 0,
    "GEO" : 0,
    "GIARDIADB" : 0,
    "GLIDA_GPCR" : 0,
    "GLIDA_LIGAND" : 0,
    "GLYCOEPITOPE" : 0,
    "GLYCOMEDB" : 0,
    "GO" : 0,
    "GO_REF" : 0,
    "GOA" : 0,
    "GOLD_GENOME" : 0,
    "GOLD_METADATA" : 0,
    "GOOGLE_PATENTS" : 0,
    "GOLM_METABOLOME_DATABASE" : 0,
    "GOLM_METABOLOME_DATABASE_ANALYTE" : 0,
    "GOLM_METABOLOME_DATABASE_GC_MS_SPECTRA" : 0,
    "GOLM_METABOLOME_DATABASE_PROFILE" : 0,
    "GOLM_METABOLOME_DATABASE_REFERENCE_SUBSTANCE" : 0,
    "GPCRDB" : 0,
    "GRAMENE_GENES" : 0,
    "GRAMENE_PROTEIN" : 0,
    "GRAMENE_QTL" : 0,
    "GRAMENE_TAXONOMY" : 0,
    "GREENGENES" : 0,
    "GRIN_PLANT_TAXONOMY" : 0,
    "GRSDB" : 0,
    "GWAS_CENRAL_MARKER" : 0,
    "GWAS_CENRAL_PHENOTYPE" : 0,
    "GWAS_CENRAL_STUDY" : 0,
    "GXA_EXPT" : 0,
    "GXA_GENE" : 0,
    "HAMAP" : 0,
    "HCVDB" : 0,
    "HGMD" : 0,
    "HGNC" : 0,
    "HGNC_FAMILY" : 0,
    "HGNC_SYMBOL" : 1,
    "H_INVDB_LOCUS" : 0,
    "H_INVDB_PROTEIN" : 0,
    "H_INVDB_TRANSCRIPT" : 0,
    "HMDB" : 0,
    "HOGENOM" : 0,
    "HOMD_SEQUENCE_METAINFORMATION" : 0,
    "HOMD_TAXONOMY" : 0,
    "HOMEODOMAIN_RESEARCH" : 0,
    "HOMOLOGENE" : 0,
    "HOVERGEN" : 0,
    "HPA" : 0,
    "HPRD" : 0,
    "HSSP" : 0,
    "HUGE" : 0,
    "HUMAN_DISEASE_ONTOLOGY" : 0,
    "HUMAN_PHENOTYPE_ONTOLOGY" : 0,
    "HUMAN_PROTEOME_MAP_PEPTIDE" : 0,
    "HUMAN_PROTEOME_MAP_PROTEIN" : 0,
    "ICD" : 0,
    "ICEBERG_ELEMENT" : 0,
    "ICEBERG_FAMILY" : 0,
    "IDEAL" : 0,
    "IDENTIFIERS_ORG_TERMS" : 0,
    "IMEX" : 0,
    "IMGT_LIGM" : 0,
    "IMGT_HLA" : 0,
    "INCHI" : 0,
    "INCHIKEY" : 0,
    "INTACT" : 0,
    "INTACT_MOLECULE" : 0,
    "INTEGRATED_MICROBIAL_GENOMES_GENE" : 0,
    "INTEGRATED_MICROBIAL_GENOMES_TAXON" : 0,
    "INTERPRO" : 0,
    "IRD_SEGMENT_SEQUENCE" : 0,
    "IREFWEB" : 0,
    "ISBN" : 0,
    "ISFINDER" : 0,
    "ISSN" : 0,
    "IUPHAR_FAMILY" : 0,
    "IUPHAR_LIGAND" : 0,
    "IUPHAR_RECEPTOR" : 0,
    "JAPAN_COLLECTION_OF_MICROORGANISMS" : 0,
    "JAPAN_CHEMICAL_SUBSTANCE_DICTIONARY" : 0,
    "JAX_MICE" : 0,
    "JCGGDB" : 0,
    "JSTOR" : 0,
    "JWS_ONLINE" : 0,
    "KEGG_COMPOUND" : 0,
    "KEGG_DISEASE" : 0,
    "KEGG_DRUG" : 0,
    "KEGG_ENVIRON" : 0,
    "KEGG_GENES" : 0,
    "KEGG_GENOME" : 0,
    "KEGG_GLYCAN" : 0,
    "KEGG_METAGENOME" : 0,
    "KEGG_MODULE" : 0,
    "KEGG_ORTHOLOGY" : 0,
    "KEGG_PATHWAY" : 0,
    "KEGG_REACTION" : 0,
    "KISAO" : 0,
    "KNAPSACK" : 0,
    "LIGANDBOX" : 0,
    "LIGAND_EXPO" : 0,
    "LIGAND_GATED_ION_CHANNEL_DATABASE" : 0,
    "LIPID_BANK" : 0,
    "LINCS_PROTEIN" : 0,
    "LINCS_CELL" : 0,
    "LIPID_MAPS" : 0,
    "LOCUS_REFERENCE_GENOMIC" : 0,
    "MACIE" : 0,
    "MAIZEGDB_LOCUS" : 0,
    "MASSBANK" : 0,
    "MATHEMATICAL_MODELLING_ONTOLOGY" : 0,
    "MATRIXDB" : 0,
    "MEDLINEPLUS" : 0,
    "MEROPS_FAMILY" : 0,
    "MEROPS_INHIBITOR" : 0,
    "MEROPS" : 0,
    "MESH_2012" : 0,
    "METANETX_CHEMICAL" : 0,
    "METANETX_COMPARTMENT" : 0,
    "METANETX_REACTION" : 0,
    "METABOLIGHTS" : 0,
    "METLIN" : 0,
    "MI" : 0,
    "MICROSPORIDIADB" : 0,
    "MICROBIAL_PROTEIN_INTERACTION_DATABASE" : 0,
    "MIMODB" : 0,
    "MIPMODDB" : 0,
    "MI_R_BASE_SEQUENCE" : 0,
    "MI_R_BASE_MATURE_SEQUENCE" : 0,
    "MIREX" : 0,
    "MIRIAM_REGISTRY_COLLECTION" : 0,
    "MIRIAM_REGISTRY_RESOURCE" : 0,
    "MIRNEST" : 0,
    "MIR_TAR_BASE_MATURE_SEQUENCE" : 0,
    "MGD" : 0,
    "MGED_ONTOLOGY" : 0,
    "MGNIFY_PROJECT" : 0,
    "MGNIFY_SAMPLE" : 0,
    "MINT" : 0,
    "MMRRC" : 0,
    "MOD" : 0,
    "MODELDB" : 0,
    "MOLBASE" : 0,
    "MOLECULAR_MODELING_DATABASE" : 0,
    "MOUSE_ADULT_GROSS_ANATOMY" : 0,
    "MYCOBANK" : 0,
    "MYCOBROWSER_LEPRAE" : 0,
    "MYCOBROWSER_MARINUM" : 0,
    "MYCOBROWSER_SMEGMATIS" : 0,
    "MYCOBROWSER_TUBERCULOSIS" : 0,
    "NAPP" : 0,
    "NARCIS" : 0,
    "NASC_CODE" : 0,
    "NATIONAL_BIBLIOGRAPHY_NUMBER" : 0,
    "NATIONAL_DRUG_CODE" : 0,
    "NCBI_PROTEIN" : 0,
    "NCIM" : 0,
    "NCI_PATHWAY_INTERACTION_DATABASE_PATHWAY" : 0,
    "NCIT" : 0,
    "NEUROLEX" : 0,
    "NEUROMORPHO" : 0,
    "NEURONDB" : 0,
    "NEXTDB" : 0,
    "NEXTPROT" : 0,
    "NIAEST" : 0,
    "NITE_BIOLOGICAL_RESEARCH_CENTER_CATALOGUE" : 0,
    "NONCODE_V3" : 0,
    "NONCODE_V4_GENE" : 0,
    "NONCODE_V4_TRANSCRIPT" : 0,
    "NORINE" : 0,
    "NUCLEARDB" : 0,
    "NUCLEOTIDE_SEQUENCE_DATABASE" : 0,
    "OBI" : 0,
    "OMA_GROUP" : 0,
    "OMA_PROTEIN" : 0,
    "ODOR_MOLECULES_DATABASE" : 0,
    "OLFACTORY_RECEPTOR_DATABASE" : 0,
    "OMIA" : 0,
    "OMIM" : 0,
    "OMIT" : 0,
    "ONTOLOGY_OF_PHYSICS_FOR_BIOLOGY" : 0,
    "OPM" : 0,
    "ORCID" : 0,
    "ORIDB_SACCHAROMYCES" : 0,
    "ORIDB_SCHIZOSACCHAROMYCES" : 0,
    "ORPHANET" : 0,
    "ORPHANET_RARE_DISEASE_ONTOLOGY" : 0,
    "ORTHODB" : 0,
    "ORYZABASE_GENE" : 0,
    "ORYZABASE_MUTANT" : 0,
    "ORYZABASE_STAGE" : 0,
    "ORYZABASE_STRAIN" : 0,
    "ORYZA_TAG_LINE" : 0,
    "P3DB_PROTEIN" : 0,
    "P3DB_SITE" : 0,
    "PALEODB" : 0,
    "PANTHER" : 0,
    "PANTHER_NODE" : 0,
    "PANTHER_PATHWAY" : 0,
    "PANTHER_PATHWAY_COMPONENT" : 0,
    "PASS2" : 0,
    "PATHWAY_ONTOLOGY" : 0,
    "PATHWAY_COMMONS" : 0,
    "PATO" : 0,
    "PAXDB_ORGANISM" : 0,
    "PAXDB_PROTEIN" : 0,
    "PAZAR_TRANSCRIPTION_FACTOR" : 0,
    "PDB" : 0,
    "PDB_CCD" : 0,
    "PEPTIDEATLAS" : 0,
    "PEROXIBASE" : 0,
    "PFAM" : 0,
    "PHARM" : 0,
    "PHARMGKB_DISEASE" : 0,
    "PHARMGKB_DRUG" : 0,
    "PHARMGKB_GENE" : 0,
    "PHENOL_EXPLORER" : 0,
    "PHOSPHOPOINT_KINASE" : 0,
    "PHOSPHOPOINT_PHOSPHOPROTEIN" : 0,
    "PHOSPHOSITE_PROTEIN" : 0,
    "PHOSPHOSITE_RESIDUE" : 0,
    "PHYLOMEDB" : 0,
    "PHYTOZOME_LOCUS" : 0,
    "PINA" : 0,
    "PIROPLASMADB" : 0,
    "PIRSF" : 0,
    "PLANT_ONTOLOGY" : 0,
    "PLASMODB" : 0,
    "PMC" : 0,
    "POCKETOME" : 0,
    "POLBASE" : 0,
    "POMBASE" : 0,
    "PRIDE" : 0,
    "PRIDE_PROJECT" : 0,
    "PRINTS" : 0,
    "PROGLYCPROT" : 0,
    "PRODOM" : 0,
    "PROSITE" : 0,
    "PROTCLUSTDB" : 0,
    "PROTEIN_AFFINITY_REAGENTS" : 0,
    "PROTEIN_DATA_BANK_LIGAND" : 0,
    "PROTEIN_MODEL_DATABASE" : 0,
    "PROTEIN_ONTOLOGY" : 0,
    "PROTEOMICSDB_PEPTIDE" : 0,
    "PROTEOMICSDB_PROTEIN" : 0,
    "PROTONET_CLUSTER" : 0,
    "PROTONET_PROTEINCARD" : 0,
    "PSCDB" : 0,
    "PSEUDOMONAS_GENOME_DATABASE" : 0,
    "PUBCHEM" : 0,
    "PUBCHEM_BIOASSAY" : 0,
    "PUBCHEM_SUBSTANCE" : 0,
    "PUBMED" : 0,
    "RAT_GENOME_DATABASE_QTL" : 0,
    "RAT_GENOME_DATABASE_STRAIN" : 0,
    "REACTOME" : 0,
    "REBASE" : 0,
    "REFSEQ" : 0,
    "RELATION_ONTOLOGY" : 0,
    "RESID" : 0,
    "RFAM" : 0,
    "RGD" : 0,
    "RHEA" : 0,
    "RICE_GENOME_ANNOTATION_PROJECT" : 0,
    "RNA_MODIFICATION_DATABASE" : 0,
    "ROUGE" : 0,
    "SABIO_RK_EC_RECORD" : 0,
    "SABIO_RK_KINETIC_RECORD" : 0,
    "SABIO_RK_REACTION" : 0,
    "SACCHAROMYCES_GENOME_DATABASE_PATHWAYS" : 0,
    "SBML_RDF_VOCABULARY" : 0,
    "SBO_TERM" : 0,
    "SCOP" : 0,
    "SCERTF" : 0,
    "SEED_COMPOUND" : 0,
    "SEED_REACTIONS" : 0,
    "SEQUENCE_ONTOLOGY" : 0,
    "SEQUENCE_READ_ARCHIVE" : 0,
    "SGD" : 0,
    "SIDER_DRUG" : 0,
    "SIDER_SIDE_EFFECT" : 0,
    "SIGNALING_GATEWAY" : 0,
    "SITEX" : 0,
    "SMALL_MOLECULE_PATHWAY_DATABASE" : 0,
    "SMART" : 0,
    "SNOMED_CT" : 0,
    "SOL_GENOMICS_NETWORK" : 0,
    "SOYBASE" : 0,
    "SPECTRAL_DATABASE_FOR_ORGANIC_COMPOUNDS" : 0,
    "SPIKE" : 0,
    "STAP" : 0,
    "STITCH" : 0,
    "STRING" : 0,
    "SUBSTRATEDB" : 0,
    "SUBTILIST" : 0,
    "SUPFAM" : 0,
    "SUBTIWIKI" : 0,
    "SWISS_LIPIDS" : 0,
    "SWISS_MODEL" : 0,
    "T3DB" : 0,
    "TAIR_GENE" : 0,
    "TAIR_PROTEIN" : 0,
    "TAIR_LOCUS" : 0,
    "TARBASE" : 0,
    "TAXONOMY" : 0,
    "TEDDY" : 0,
    "TETRAHYMENA_GENOME_DATABASE" : 0,
    "TIGRFAMS" : 0,
    "TISSUE_LIST" : 0,
    "TOPDB" : 0,
    "TOPFIND" : 0,
    "TOXICOGENOMIC_CHEMICAL" : 0,
    "TOXODB" : 0,
    "TREEBASE" : 0,
    "TREEFAM" : 0,
    "TREE_OF_LIFE" : 0,
    "TRICHDB" : 0,
    "TRITRYPDB" : 0,
    "TTD_Drug" : 0,
    "TTD_TARGET" : 0,
    "TRANSPORT_CLASSIFICATION_DATABASE" : 0,
    "UBERON" : 0,
    "UBIO_NAMEBANK" : 0,
    "UM_BBD_COMPOUND" : 0,
    "UM_BBD_ENZYME" : 0,
    "UM_BBD_PATHWAY" : 0,
    "UM_BBD_REACTION" : 0,
    "UM_BBD_BIOTRANSFORMATION_RULE" : 0,
    "UNIGENE" : 0,
    "UNII" : 0,
    "UNIMOD" : 0,
    "UNIPARC" : 0,
    "UNIPATHWAY_REACTION" : 0,
    "UNIPROT" : 0,
    "UNIPROT_ISOFORM" : 0,
    "UNISTS" : 0,
    "UNIT_ONTOLOGY" : 0,
    "UNITE" : 0,
    "USPTO" : 0,
    "UNKNOWN" : 0,
    "VARIO" : 0,
    "VBASE2" : 0,
    "VBRC" : 0,
    "VFDB_GENE" : 0,
    "VFDB_GENUS" : 0,
    "VIRALZONE" : 0,
    "VIRSIRNA" : 0,
    "VMH_METABOLITE" : 0,
    "VMH_REACTION" : 0,
    "WIKIDATA" : 0,
    "WIKIGENES" : 0,
    "WIKIPATHWAYS" : 0,
    "WIKIPEDIA" : 0,
    "WORFDB" : 0,
    "WORM_BASE" : 0,
    "WORM_BASE_RNAI" : 0,
    "WORMPEP" : 0,
    "XENBASE" : 0,
    "YDPM" : 0,
    "YEAST_INTRON_DATABASE_V4_3" : 0,
    "YETFASCO" : 0,
    "YEAST_INTRON_DATABASE_V3" : 0,
    "YRC_PDR" : 0,
    "ZFIN" : 0,
    "ZINC" : 0
  },
  "publications" : 2,
  "reactionAnnotations" : {
    "_3DMET" : 0,
    "ABS" : 0,
    "ACEVIEW_WORM" : 0,
    "AFFYMETRIX_PROBESET" : 0,
    "AFTOL" : 0,
    "ALLERGOME" : 0,
    "AMOEBADB" : 0,
    "ANATOMICAL_THERAPEUTIC_CHEMICAL" : 0,
    "ANATOMICAL_THERAPEUTIC_CHEMICAL_VETINARY" : 0,
    "ANIMAL_DIVERSITY_WEB" : 0,
    "ANIMAL_GENOME_CATTLE_QTL" : 0,
    "ANIMAL_GENOME_CHICKEN_QTL" : 0,
    "ANIMAL_GENOME_PIG_QTL" : 0,
    "ANIMAL_GENOME_SHEEP_QTL" : 0,
    "ANIMAL_TFDB_FAMILY" : 0,
    "ANTIBIOTIC_RESISTANCE_GENES_DATABASE" : 0,
    "ANTIBODY_REGISTRY" : 0,
    "ANTWEB" : 0,
    "APD" : 0,
    "APHIDBASE_TRANSCRIPT" : 0,
    "ARACHNOSERVER" : 0,
    "ARRAYEXPRESS" : 0,
    "ARRAYEXPRESS_PLATFORM" : 0,
    "ARXIV" : 0,
    "ASAP" : 0,
    "ASPGD_LOCUS" : 0,
    "ASPGD_PROTEIN" : 0,
    "ATCC" : 0,
    "AUTDB" : 0,
    "BACMAP_BIOGRAPHY" : 0,
    "BACMAP_MAP" : 0,
    "BDGP_EST" : 0,
    "BDGP_INSERTION_DB" : 0,
    "BEETLEBASE" : 0,
    "BGEE_FAMILY" : 0,
    "BGEE_GENE" : 0,
    "BGEE_ORGAN" : 0,
    "BGEE_STAGE" : 0,
    "BiGG_COMPARTMENT" : 0,
    "BiGG_METABOLITE" : 0,
    "BiGG_REACTIONS" : 0,
    "BINDINGDB" : 0,
    "BIOCARTA_PATHWAY" : 0,
    "BIOCATALOGUE" : 0,
    "BIOCYC" : 0,
    "BIOGRID" : 0,
    "BIOKC" : 0,
    "BIOMODELS_DATABASE" : 0,
    "BIONUMBERS" : 0,
    "BIOPORTAL" : 0,
    "BIOPROJECT" : 0,
    "BIOSAMPLE" : 0,
    "BIOSYSTEMS" : 0,
    "BITTERDB_COMPOUND" : 0,
    "BITTERDB_RECEPTOR" : 0,
    "BOLD_TAXONOMY" : 0,
    "BROAD_FUNGAL_GENOME_INITIATIVE" : 0,
    "BRENDA" : 0,
    "BRENDA_TISSUE_ONTOLOGY" : 0,
    "BUGBASE_EXPT" : 0,
    "BUGBASE_PROTOCOL" : 0,
    "BYKDB" : 0,
    "CANADIAN_DRUG_PRODUCT_DATABASE" : 0,
    "CANDIDA_GENOME_DATABASE" : 0,
    "CAPS_DB" : 0,
    "CAS" : 0,
    "CATH_DOMAIN" : 0,
    "CATH_SUPERFAMILY" : 0,
    "CAZY" : 0,
    "CCDS" : 0,
    "CELL_CYCLE_ONTOLOGY" : 0,
    "CELL_IMAGE_LIBRARY" : 0,
    "CELL_SIGNALING_TECHNOLOGY_PATHWAYS" : 0,
    "CELL_SIGNALING_TECHNOLOGY_ANTIBODY" : 0,
    "CELL_TYPE_ONTOLOGY" : 0,
    "CGSC_STRAIN" : 0,
    "CHARPROT" : 0,
    "CHEBI" : 0,
    "CHEMDB" : 0,
    "CHEM_ID_PLUS" : 0,
    "CHEMSPIDER" : 0,
    "CHEMBL_COMPOUND" : 0,
    "CHEMBL_TARGET" : 0,
    "CLDB" : 0,
    "CLINICAL_TRIALS_GOV" : 0,
    "CLINVAR_RECORD" : 0,
    "COG" : 0,
    "COMBINE_SPECIFICATIONS" : 0,
    "COMPLEX_PORTAL" : 0,
    "COMPULYEAST" : 0,
    "CONSERVED_DOMAIN_DATABASE" : 0,
    "CONOSERVER" : 0,
    "CORIELL_CELL_REPOSITORIES" : 0,
    "CORUM" : 0,
    "CPC" : 0,
    "CRYPTODB" : 0,
    "CSA" : 0,
    "CTD_GENE" : 0,
    "CTD_DISEASE" : 0,
    "CUTDB" : 0,
    "CUBE_DB" : 0,
    "DAILYMED" : 0,
    "DARC" : 0,
    "DATABASE_OF_INTERACTING_PROTEINS" : 0,
    "DATABASE_OF_QUANTITATIVE_CELLULAR_SIGNALING_MODEL" : 0,
    "DATABASE_OF_QUANTITATIVE_CELLULAR_SIGNALING_PATHWAY" : 0,
    "DATF" : 0,
    "DBD" : 0,
    "DBEST" : 0,
    "DBG2_INTRONS" : 0,
    "DBPROBE" : 0,
    "DB_SNP" : 0,
    "DEGRADOME_DATABASE" : 0,
    "DEPOD" : 0,
    "DICTYBASE_EST" : 0,
    "DICTYBASE_GENE" : 0,
    "DISPROT" : 0,
    "DOI" : 0,
    "DOMMINO" : 0,
    "DOOR" : 0,
    "DPV" : 0,
    "DRAGONDB_ALLELE" : 0,
    "DRAGONDB_DNA" : 0,
    "DRAGONDB_LOCUS" : 0,
    "DRAGONDB_PROTEIN" : 0,
    "DRSC" : 0,
    "DRUGBANK" : 0,
    "DRUGBANK_TARGET_V4" : 0,
    "EC" : 0,
    "ECHOBASE" : 0,
    "ECO" : 0,
    "ECOGENE" : 0,
    "ECOLIWIKI" : 0,
    "EDAM_ONTOLOGY" : 0,
    "EGGNOG" : 0,
    "ELM" : 0,
    "ENA" : 0,
    "ENSEMBL" : 0,
    "ENSEMBL_BACTERIA" : 0,
    "ENSEMBL_FUNGI" : 0,
    "ENSEMBL_METAZOA" : 0,
    "ENSEMBL_PLANTS" : 0,
    "ENSEMBL_PROTISTS" : 0,
    "ENTREZ" : 0,
    "ENVIPATH" : 0,
    "EPD" : 0,
    "EU_CLINICAL_TRIALS" : 0,
    "EXAC_GENE" : 0,
    "EXAC_TRANSCRIPT" : 0,
    "EXAC_VARIANT" : 0,
    "EXPERIMENTAL_FACTOR_ONTOLOGY" : 0,
    "EUROPEAN_GENOME_PHENOME_ARCHIVE_DATASET" : 0,
    "EUROPEAN_GENOME_PHENOME_ARCHIVE_STUDY" : 0,
    "FMA" : 0,
    "FOODB_COMPOUND" : 0,
    "F_SNP" : 0,
    "FUNCBASE_FLY" : 0,
    "FUNCBASE_HUMAN" : 0,
    "FUNCBASE_MOUSE" : 0,
    "FUNCBASE_YEAST" : 0,
    "FUNGIDB" : 0,
    "FLYBASE" : 0,
    "GABI" : 0,
    "GENATLAS" : 0,
    "GENECARDS" : 0,
    "GENE_DB" : 0,
    "GENEFARM" : 0,
    "GENETREE" : 0,
    "GENE_WIKI" : 0,
    "GENPEPT" : 0,
    "GENOME_PROPERTIES" : 0,
    "GENOMIC_DATA_COMMONS_DATA_PORTAL" : 0,
    "GEO" : 0,
    "GIARDIADB" : 0,
    "GLIDA_GPCR" : 0,
    "GLIDA_LIGAND" : 0,
    "GLYCOEPITOPE" : 0,
    "GLYCOMEDB" : 0,
    "GO" : 0,
    "GO_REF" : 0,
    "GOA" : 0,
    "GOLD_GENOME" : 0,
    "GOLD_METADATA" : 0,
    "GOOGLE_PATENTS" : 0,
    "GOLM_METABOLOME_DATABASE" : 0,
    "GOLM_METABOLOME_DATABASE_ANALYTE" : 0,
    "GOLM_METABOLOME_DATABASE_GC_MS_SPECTRA" : 0,
    "GOLM_METABOLOME_DATABASE_PROFILE" : 0,
    "GOLM_METABOLOME_DATABASE_REFERENCE_SUBSTANCE" : 0,
    "GPCRDB" : 0,
    "GRAMENE_GENES" : 0,
    "GRAMENE_PROTEIN" : 0,
    "GRAMENE_QTL" : 0,
    "GRAMENE_TAXONOMY" : 0,
    "GREENGENES" : 0,
    "GRIN_PLANT_TAXONOMY" : 0,
    "GRSDB" : 0,
    "GWAS_CENRAL_MARKER" : 0,
    "GWAS_CENRAL_PHENOTYPE" : 0,
    "GWAS_CENRAL_STUDY" : 0,
    "GXA_EXPT" : 0,
    "GXA_GENE" : 0,
    "HAMAP" : 0,
    "HCVDB" : 0,
    "HGMD" : 0,
    "HGNC" : 0,
    "HGNC_FAMILY" : 0,
    "HGNC_SYMBOL" : 0,
    "H_INVDB_LOCUS" : 0,
    "H_INVDB_PROTEIN" : 0,
    "H_INVDB_TRANSCRIPT" : 0,
    "HMDB" : 0,
    "HOGENOM" : 0,
    "HOMD_SEQUENCE_METAINFORMATION" : 0,
    "HOMD_TAXONOMY" : 0,
    "HOMEODOMAIN_RESEARCH" : 0,
    "HOMOLOGENE" : 0,
    "HOVERGEN" : 0,
    "HPA" : 0,
    "HPRD" : 0,
    "HSSP" : 0,
    "HUGE" : 0,
    "HUMAN_DISEASE_ONTOLOGY" : 0,
    "HUMAN_PHENOTYPE_ONTOLOGY" : 0,
    "HUMAN_PROTEOME_MAP_PEPTIDE" : 0,
    "HUMAN_PROTEOME_MAP_PROTEIN" : 0,
    "ICD" : 0,
    "ICEBERG_ELEMENT" : 0,
    "ICEBERG_FAMILY" : 0,
    "IDEAL" : 0,
    "IDENTIFIERS_ORG_TERMS" : 0,
    "IMEX" : 0,
    "IMGT_LIGM" : 0,
    "IMGT_HLA" : 0,
    "INCHI" : 0,
    "INCHIKEY" : 0,
    "INTACT" : 0,
    "INTACT_MOLECULE" : 0,
    "INTEGRATED_MICROBIAL_GENOMES_GENE" : 0,
    "INTEGRATED_MICROBIAL_GENOMES_TAXON" : 0,
    "INTERPRO" : 0,
    "IRD_SEGMENT_SEQUENCE" : 0,
    "IREFWEB" : 0,
    "ISBN" : 0,
    "ISFINDER" : 0,
    "ISSN" : 0,
    "IUPHAR_FAMILY" : 0,
    "IUPHAR_LIGAND" : 0,
    "IUPHAR_RECEPTOR" : 0,
    "JAPAN_COLLECTION_OF_MICROORGANISMS" : 0,
    "JAPAN_CHEMICAL_SUBSTANCE_DICTIONARY" : 0,
    "JAX_MICE" : 0,
    "JCGGDB" : 0,
    "JSTOR" : 0,
    "JWS_ONLINE" : 0,
    "KEGG_COMPOUND" : 0,
    "KEGG_DISEASE" : 0,
    "KEGG_DRUG" : 0,
    "KEGG_ENVIRON" : 0,
    "KEGG_GENES" : 0,
    "KEGG_GENOME" : 0,
    "KEGG_GLYCAN" : 0,
    "KEGG_METAGENOME" : 0,
    "KEGG_MODULE" : 0,
    "KEGG_ORTHOLOGY" : 0,
    "KEGG_PATHWAY" : 0,
    "KEGG_REACTION" : 0,
    "KISAO" : 0,
    "KNAPSACK" : 0,
    "LIGANDBOX" : 0,
    "LIGAND_EXPO" : 0,
    "LIGAND_GATED_ION_CHANNEL_DATABASE" : 0,
    "LIPID_BANK" : 0,
    "LINCS_PROTEIN" : 0,
    "LINCS_CELL" : 0,
    "LIPID_MAPS" : 0,
    "LOCUS_REFERENCE_GENOMIC" : 0,
    "MACIE" : 0,
    "MAIZEGDB_LOCUS" : 0,
    "MASSBANK" : 0,
    "MATHEMATICAL_MODELLING_ONTOLOGY" : 0,
    "MATRIXDB" : 0,
    "MEDLINEPLUS" : 0,
    "MEROPS_FAMILY" : 0,
    "MEROPS_INHIBITOR" : 0,
    "MEROPS" : 0,
    "MESH_2012" : 0,
    "METANETX_CHEMICAL" : 0,
    "METANETX_COMPARTMENT" : 0,
    "METANETX_REACTION" : 0,
    "METABOLIGHTS" : 0,
    "METLIN" : 0,
    "MI" : 0,
    "MICROSPORIDIADB" : 0,
    "MICROBIAL_PROTEIN_INTERACTION_DATABASE" : 0,
    "MIMODB" : 0,
    "MIPMODDB" : 0,
    "MI_R_BASE_SEQUENCE" : 0,
    "MI_R_BASE_MATURE_SEQUENCE" : 0,
    "MIREX" : 0,
    "MIRIAM_REGISTRY_COLLECTION" : 0,
    "MIRIAM_REGISTRY_RESOURCE" : 0,
    "MIRNEST" : 0,
    "MIR_TAR_BASE_MATURE_SEQUENCE" : 0,
    "MGD" : 0,
    "MGED_ONTOLOGY" : 0,
    "MGNIFY_PROJECT" : 0,
    "MGNIFY_SAMPLE" : 0,
    "MINT" : 0,
    "MMRRC" : 0,
    "MOD" : 0,
    "MODELDB" : 0,
    "MOLBASE" : 0,
    "MOLECULAR_MODELING_DATABASE" : 0,
    "MOUSE_ADULT_GROSS_ANATOMY" : 0,
    "MYCOBANK" : 0,
    "MYCOBROWSER_LEPRAE" : 0,
    "MYCOBROWSER_MARINUM" : 0,
    "MYCOBROWSER_SMEGMATIS" : 0,
    "MYCOBROWSER_TUBERCULOSIS" : 0,
    "NAPP" : 0,
    "NARCIS" : 0,
    "NASC_CODE" : 0,
    "NATIONAL_BIBLIOGRAPHY_NUMBER" : 0,
    "NATIONAL_DRUG_CODE" : 0,
    "NCBI_PROTEIN" : 0,
    "NCIM" : 0,
    "NCI_PATHWAY_INTERACTION_DATABASE_PATHWAY" : 0,
    "NCIT" : 0,
    "NEUROLEX" : 0,
    "NEUROMORPHO" : 0,
    "NEURONDB" : 0,
    "NEXTDB" : 0,
    "NEXTPROT" : 0,
    "NIAEST" : 0,
    "NITE_BIOLOGICAL_RESEARCH_CENTER_CATALOGUE" : 0,
    "NONCODE_V3" : 0,
    "NONCODE_V4_GENE" : 0,
    "NONCODE_V4_TRANSCRIPT" : 0,
    "NORINE" : 0,
    "NUCLEARDB" : 0,
    "NUCLEOTIDE_SEQUENCE_DATABASE" : 0,
    "OBI" : 0,
    "OMA_GROUP" : 0,
    "OMA_PROTEIN" : 0,
    "ODOR_MOLECULES_DATABASE" : 0,
    "OLFACTORY_RECEPTOR_DATABASE" : 0,
    "OMIA" : 0,
    "OMIM" : 0,
    "OMIT" : 0,
    "ONTOLOGY_OF_PHYSICS_FOR_BIOLOGY" : 0,
    "OPM" : 0,
    "ORCID" : 0,
    "ORIDB_SACCHAROMYCES" : 0,
    "ORIDB_SCHIZOSACCHAROMYCES" : 0,
    "ORPHANET" : 0,
    "ORPHANET_RARE_DISEASE_ONTOLOGY" : 0,
    "ORTHODB" : 0,
    "ORYZABASE_GENE" : 0,
    "ORYZABASE_MUTANT" : 0,
    "ORYZABASE_STAGE" : 0,
    "ORYZABASE_STRAIN" : 0,
    "ORYZA_TAG_LINE" : 0,
    "P3DB_PROTEIN" : 0,
    "P3DB_SITE" : 0,
    "PALEODB" : 0,
    "PANTHER" : 0,
    "PANTHER_NODE" : 0,
    "PANTHER_PATHWAY" : 0,
    "PANTHER_PATHWAY_COMPONENT" : 0,
    "PASS2" : 0,
    "PATHWAY_ONTOLOGY" : 0,
    "PATHWAY_COMMONS" : 0,
    "PATO" : 0,
    "PAXDB_ORGANISM" : 0,
    "PAXDB_PROTEIN" : 0,
    "PAZAR_TRANSCRIPTION_FACTOR" : 0,
    "PDB" : 0,
    "PDB_CCD" : 0,
    "PEPTIDEATLAS" : 0,
    "PEROXIBASE" : 0,
    "PFAM" : 0,
    "PHARM" : 0,
    "PHARMGKB_DISEASE" : 0,
    "PHARMGKB_DRUG" : 0,
    "PHARMGKB_GENE" : 0,
    "PHENOL_EXPLORER" : 0,
    "PHOSPHOPOINT_KINASE" : 0,
    "PHOSPHOPOINT_PHOSPHOPROTEIN" : 0,
    "PHOSPHOSITE_PROTEIN" : 0,
    "PHOSPHOSITE_RESIDUE" : 0,
    "PHYLOMEDB" : 0,
    "PHYTOZOME_LOCUS" : 0,
    "PINA" : 0,
    "PIROPLASMADB" : 0,
    "PIRSF" : 0,
    "PLANT_ONTOLOGY" : 0,
    "PLASMODB" : 0,
    "PMC" : 0,
    "POCKETOME" : 0,
    "POLBASE" : 0,
    "POMBASE" : 0,
    "PRIDE" : 0,
    "PRIDE_PROJECT" : 0,
    "PRINTS" : 0,
    "PROGLYCPROT" : 0,
    "PRODOM" : 0,
    "PROSITE" : 0,
    "PROTCLUSTDB" : 0,
    "PROTEIN_AFFINITY_REAGENTS" : 0,
    "PROTEIN_DATA_BANK_LIGAND" : 0,
    "PROTEIN_MODEL_DATABASE" : 0,
    "PROTEIN_ONTOLOGY" : 0,
    "PROTEOMICSDB_PEPTIDE" : 0,
    "PROTEOMICSDB_PROTEIN" : 0,
    "PROTONET_CLUSTER" : 0,
    "PROTONET_PROTEINCARD" : 0,
    "PSCDB" : 0,
    "PSEUDOMONAS_GENOME_DATABASE" : 0,
    "PUBCHEM" : 0,
    "PUBCHEM_BIOASSAY" : 0,
    "PUBCHEM_SUBSTANCE" : 0,
    "PUBMED" : 2,
    "RAT_GENOME_DATABASE_QTL" : 0,
    "RAT_GENOME_DATABASE_STRAIN" : 0,
    "REACTOME" : 0,
    "REBASE" : 0,
    "REFSEQ" : 0,
    "RELATION_ONTOLOGY" : 0,
    "RESID" : 0,
    "RFAM" : 0,
    "RGD" : 0,
    "RHEA" : 0,
    "RICE_GENOME_ANNOTATION_PROJECT" : 0,
    "RNA_MODIFICATION_DATABASE" : 0,
    "ROUGE" : 0,
    "SABIO_RK_EC_RECORD" : 0,
    "SABIO_RK_KINETIC_RECORD" : 0,
    "SABIO_RK_REACTION" : 0,
    "SACCHAROMYCES_GENOME_DATABASE_PATHWAYS" : 0,
    "SBML_RDF_VOCABULARY" : 0,
    "SBO_TERM" : 0,
    "SCOP" : 0,
    "SCERTF" : 0,
    "SEED_COMPOUND" : 0,
    "SEED_REACTIONS" : 0,
    "SEQUENCE_ONTOLOGY" : 0,
    "SEQUENCE_READ_ARCHIVE" : 0,
    "SGD" : 0,
    "SIDER_DRUG" : 0,
    "SIDER_SIDE_EFFECT" : 0,
    "SIGNALING_GATEWAY" : 0,
    "SITEX" : 0,
    "SMALL_MOLECULE_PATHWAY_DATABASE" : 0,
    "SMART" : 0,
    "SNOMED_CT" : 0,
    "SOL_GENOMICS_NETWORK" : 0,
    "SOYBASE" : 0,
    "SPECTRAL_DATABASE_FOR_ORGANIC_COMPOUNDS" : 0,
    "SPIKE" : 0,
    "STAP" : 0,
    "STITCH" : 0,
    "STRING" : 0,
    "SUBSTRATEDB" : 0,
    "SUBTILIST" : 0,
    "SUPFAM" : 0,
    "SUBTIWIKI" : 0,
    "SWISS_LIPIDS" : 0,
    "SWISS_MODEL" : 0,
    "T3DB" : 0,
    "TAIR_GENE" : 0,
    "TAIR_PROTEIN" : 0,
    "TAIR_LOCUS" : 0,
    "TARBASE" : 0,
    "TAXONOMY" : 0,
    "TEDDY" : 0,
    "TETRAHYMENA_GENOME_DATABASE" : 0,
    "TIGRFAMS" : 0,
    "TISSUE_LIST" : 0,
    "TOPDB" : 0,
    "TOPFIND" : 0,
    "TOXICOGENOMIC_CHEMICAL" : 0,
    "TOXODB" : 0,
    "TREEBASE" : 0,
    "TREEFAM" : 0,
    "TREE_OF_LIFE" : 0,
    "TRICHDB" : 0,
    "TRITRYPDB" : 0,
    "TTD_Drug" : 0,
    "TTD_TARGET" : 0,
    "TRANSPORT_CLASSIFICATION_DATABASE" : 0,
    "UBERON" : 0,
    "UBIO_NAMEBANK" : 0,
    "UM_BBD_COMPOUND" : 0,
    "UM_BBD_ENZYME" : 0,
    "UM_BBD_PATHWAY" : 0,
    "UM_BBD_REACTION" : 0,
    "UM_BBD_BIOTRANSFORMATION_RULE" : 0,
    "UNIGENE" : 0,
    "UNII" : 0,
    "UNIMOD" : 0,
    "UNIPARC" : 0,
    "UNIPATHWAY_REACTION" : 0,
    "UNIPROT" : 0,
    "UNIPROT_ISOFORM" : 0,
    "UNISTS" : 0,
    "UNIT_ONTOLOGY" : 0,
    "UNITE" : 0,
    "USPTO" : 0,
    "UNKNOWN" : 0,
    "VARIO" : 0,
    "VBASE2" : 0,
    "VBRC" : 0,
    "VFDB_GENE" : 0,
    "VFDB_GENUS" : 0,
    "VIRALZONE" : 0,
    "VIRSIRNA" : 0,
    "VMH_METABOLITE" : 0,
    "VMH_REACTION" : 0,
    "WIKIDATA" : 0,
    "WIKIGENES" : 0,
    "WIKIPATHWAYS" : 0,
    "WIKIPEDIA" : 0,
    "WORFDB" : 0,
    "WORM_BASE" : 0,
    "WORM_BASE_RNAI" : 0,
    "WORMPEP" : 0,
    "XENBASE" : 0,
    "YDPM" : 0,
    "YEAST_INTRON_DATABASE_V4_3" : 0,
    "YETFASCO" : 0,
    "YEAST_INTRON_DATABASE_V3" : 0,
    "YRC_PDR" : 0,
    "ZFIN" : 0,
    "ZINC" : 0
  }
}
```

1. List backgrounds
1.1. Path Parameters
Table 1. /minerva/api/projects/{projectId}/backgrounds/
Parameter	Description
projectId

project identifier

1.2. Response Fields
Path	Type	Description
[].id

Number

identifier

[].name

String

name

[].description

String

description

[].project.projectId

String

project id where this background belongs to

[].creator.login

String

who created background

[].status

String

is the background ready. Available statuses are: FAILURE, GENERATING, NA, OK, UNKNOWN

[].progress

Number

generating images progress information (in %)

[].order

Number

order used when listing all backgrounds

[].images[].path

String

directory where background tiles are located

[].images[].model.id

Number

(sub)map for which images are described

[].defaultOverlay

Boolean

should the background be used as default (at most one per project should be marked with true)

1.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/backgrounds/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.4. Sample Response
[ {
  "id" : 412,
  "name" : "Normal",
  "defaultOverlay" : true,
  "project" : {
    "projectId" : "test_project"
  },
  "creator" : {
    "login" : "admin"
  },
  "status" : "OK",
  "progress" : 100.0,
  "description" : null,
  "order" : 0,
  "images" : [ {
    "id" : 779,
    "model" : {
      "id" : 747
    },
    "projectBackground" : {
      "id" : 412
    },
    "path" : "directory_1"
  }, {
    "id" : 778,
    "model" : {
      "id" : 746
    },
    "projectBackground" : {
      "id" : 412
    },
    "path" : "directory_0"
  } ]
} ]
2. Get background by id
2.1. Path Parameters
Table 2. /minerva/api/projects/{projectId}/backgrounds/{backgroundId}
Parameter	Description
projectId

project identifier

backgroundId

background identifier

2.2. Response Fields
Path	Type	Description
id

Number

identifier

name

String

name

description

String

description

project.projectId

String

project id where this background belongs to

creator.login

String

who created background

status

String

is the background ready. Available statuses are: FAILURE, GENERATING, NA, OK, UNKNOWN

progress

Number

generating images progress information (in %)

order

Number

order used when listing all backgrounds

images[].path

String

directory where background tiles are located

images[].model.id

Number

(sub)map for which images are described

defaultOverlay

Boolean

should the background be used as default (at most one per project should be marked with true)

2.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/backgrounds/397' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
2.4. Sample Response
{
  "id" : 397,
  "name" : "Normal",
  "defaultOverlay" : true,
  "project" : {
    "projectId" : "test_project"
  },
  "creator" : {
    "login" : "admin"
  },
  "status" : "OK",
  "progress" : 100.0,
  "description" : null,
  "order" : 0,
  "images" : [ {
    "id" : 758,
    "model" : {
      "id" : 731
    },
    "projectBackground" : {
      "id" : 397
    },
    "path" : "directory_1"
  }, {
    "id" : 757,
    "model" : {
      "id" : 732
    },
    "projectBackground" : {
      "id" : 397
    },
    "path" : "directory_0"
  } ]
}
3. Update Background
3.1. Path Parameters
Table 3. /minerva/api/projects/{projectId}/backgrounds/{backgroundId}
Parameter	Description
projectId

project identifier

backgroundId

background identifier

3.2. Request Fields
Path	Type	Description
id

Number

identifier

name

String

name

description

String

description

creator

String

who created background

order

Number

order used when listing all backgrounds

defaultOverlay

Boolean

should the background be used as default (at most one per project should be marked with true)

3.3. Response Fields
Path	Type	Description
id

Number

identifier

name

String

name

description

String

description

project.projectId

String

project id where this background belongs to

creator.login

String

who created background

status

String

is the background ready. Available statuses are: FAILURE, GENERATING, NA, OK, UNKNOWN

progress

Number

generating images progress information (in %)

order

Number

order used when listing all backgrounds

images[].path

String

directory where background tiles are located

images[].model.id

Number

(sub)map for which images are described

defaultOverlay

Boolean

should the background be used as default (at most one per project should be marked with true)

3.4. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/backgrounds/392' -X PATCH \
    -d '{"id":392,"name":"weird_title","defaultOverlay":false,"creator":"admin","description":"new description","order":0}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
3.5. Sample Response
{
  "id" : 392,
  "name" : "weird_title",
  "defaultOverlay" : false,
  "project" : {
    "projectId" : "test_project"
  },
  "creator" : {
    "login" : "admin"
  },
  "status" : "OK",
  "progress" : 100.0,
  "description" : "new description",
  "order" : 0,
  "images" : [ {
    "id" : 750,
    "model" : {
      "id" : 726
    },
    "projectBackground" : {
      "id" : 392
    },
    "path" : "directory_1"
  }, {
    "id" : 751,
    "model" : {
      "id" : 727
    },
    "projectBackground" : {
      "id" : 392
    },
    "path" : "directory_0"
  } ]
}
4. Delete overlay
4.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/backgrounds/426' -X DELETE \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
4.2. Path Parameters
Table 4. /minerva/api/projects/{projectId}/backgrounds/{backgroundId}
Parameter	Description
projectId

project identifier

backgroundId

background identifier

1. Get chemical
Returns chemicals data with project related connections.

1.1. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/TEST_PROJECT/chemicals:search?query=stilbene%20oxide' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.2. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/TEST_PROJECT/chemicals:search?target=ALIAS:756' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.3. Path Parameters
Table 1. /minerva/api/projects/{projectId}/chemicals:search
Parameter	Description
projectId

project identifier

1.4. Request Parameters
Parameter	Description
columns

set of columns (all by default). Available options: name, references, description, synonyms, id, directEvidenceReferences, directEvidence, targets

query

name of chemical that we are searching for

target

target element that we are searching for in format TYPE:ID

1.5. Response Fields
Path	Type	Description
[].id

object

identifier of the chemical

[].name

string

name

[].description

string

description

[].synonyms

array<string>

list of synonyms

[].references

array<Reference>

list of references

[].targets

array<Target>

list of targets

[].targets[].name

string

target name

[].targets[].references

array<Reference>

list of target references

[].targets[].targetElements

array<object>

list of elements on the map associated with this target

[].targets[].targetParticipants

array<object>

list of identifiers associated with this target

[].directEvidence

string

direct evidence

[].directEvidenceReferences

array<Reference>

list of references

1.6. Sample Response
[ {
  "name" : "stilbene oxide",
  "references" : [ {
    "link" : "http://id.nlm.nih.gov/mesh/C025906",
    "type" : "MESH_2012",
    "resource" : "C025906",
    "id" : 0,
    "annotatorClassName" : ""
  } ],
  "description" : null,
  "synonyms" : [ "stilbene oxide, (cis)-isomer", "stilbene oxide, (trans)-isomer", "stilbene oxide, trans-", "stilbene oxide, (2S-trans)-isomer", "stilbene oxide, (2R-trans)-isomer", "trans-stilbene oxide", "stilbene oxide, trans-(+-)-isomer" ],
  "id" : {
    "link" : "http://id.nlm.nih.gov/mesh/C025906",
    "type" : "MESH_2012",
    "resource" : "C025906",
    "id" : 0,
    "annotatorClassName" : ""
  },
  "directEvidenceReferences" : [ ],
  "directEvidence" : null,
  "targets" : [ {
    "name" : "GSTA4",
    "targetParticipants" : [ {
      "link" : "https://www.genenames.org/data/gene-symbol-report/#!/symbol/GSTA4",
      "type" : "HGNC_SYMBOL",
      "resource" : "GSTA4",
      "id" : 0,
      "annotatorClassName" : ""
    } ],
    "references" : [ {
      "link" : "https://pubmed.ncbi.nlm.nih.gov/16510128/",
      "article" : null,
      "type" : "PUBMED",
      "resource" : "16510128",
      "id" : 0,
      "annotatorClassName" : ""
    } ],
    "targetElements" : [ {
      "id" : 713,
      "modelId" : 284,
      "type" : "ALIAS"
    }, {
      "id" : 712,
      "modelId" : 285,
      "type" : "ALIAS"
    }, {
      "id" : 713,
      "modelId" : 284,
      "type" : "ALIAS"
    } ]
  }, {
    "name" : "GSTP1",
    "targetParticipants" : [ {
      "link" : "https://www.genenames.org/data/gene-symbol-report/#!/symbol/GSTP1",
      "type" : "HGNC_SYMBOL",
      "resource" : "GSTP1",
      "id" : 0,
      "annotatorClassName" : ""
    } ],
    "references" : [ {
      "link" : "https://pubmed.ncbi.nlm.nih.gov/23721876/",
      "article" : null,
      "type" : "PUBMED",
      "resource" : "23721876",
      "id" : 0,
      "annotatorClassName" : ""
    }, {
      "link" : "https://pubmed.ncbi.nlm.nih.gov/17190945/",
      "article" : null,
      "type" : "PUBMED",
      "resource" : "17190945",
      "id" : 0,
      "annotatorClassName" : ""
    } ],
    "targetElements" : [ ]
  } ]
} ]
2. Get suggested chemical queries
Get list of suggested chemical queries in the context of the project.

2.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/TEST_PROJECT2/chemicals/suggestedQueryList' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
2.2. Path Parameters
Table 2. /minerva/api/projects/{projectId}/chemicals/suggestedQueryList
Parameter	Description
projectId

project identifier

2.3. Response Fields
Path	Type	Description
[]

array<string>

list of suggested chemical queries

2.4. Sample Response
[ ]

1. Get comments
Get list of comments.

1.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/comments/models/307/?columns=author,elementId,content' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.2. Path Parameters
Table 1. /minerva/api/projects/{projectId}/comments/models/{mapId}/
Parameter	Description
projectId

project identifier

mapId

map identifier

1.3. Request Parameters
Parameter	Description
columns

set of columns (all by default). Available options: title, icon, type, content, removed, coord, modelId, elementId, id, pinned, email, owner, removeReason

removed

true/false/undefined - when defined comment property must match this parameter

1.4. Response Fields
Path	Type	Description
[]

array<Comment>

list of comments

[].owner

string

login of the user that created a comment

[].email

string

author email address

[].content

string

content

[].title

string

formatted name of the commented element

[].pinned

boolean

should the comment be visible to everybody on the map

[].removed

boolean

is the comment removed

[].removeReason

string

reason why comment was removed

[].id

integer

comment identifier

[].modelId

integer

map identifier

[].coord

point

coordinates where comment should be pinned

[].icon

string

icon that should be used to visualize this comment

[].elementId

string

element identifier

[].type

string

type of the element that was commented on. Available options ALIAS, POINT, REACTION

1.5. Sample Response
[ {
  "content" : null,
  "elementId" : "10.00,20.00"
}, {
  "content" : null,
  "elementId" : "10.00,20.00"
}, {
  "content" : null,
  "elementId" : "10.00,20.00"
} ]
2. Get comments for specific reaction
2.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/comments/models/311/bioEntities/reactions/159' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
2.2. Path Parameters
Table 2. /minerva/api/projects/{projectId}/comments/models/{mapId}/bioEntities/reactions/{reactionId}
Parameter	Description
projectId

project identifier

mapId

map identifier

reactionId

reaction identifier

2.3. Request Parameters
Parameter	Description
columns

set of columns (all by default). Available options: title, icon, type, content, removed, coord, modelId, elementId, id, pinned, email, owner, removeReason

removed

true/false/undefined - when defined comment property must match this parameter

2.4. Response Fields
Path	Type	Description
[]

array<Comment>

list of comments

[].owner

string

login of the user that created a comment

[].email

string

author email address

[].content

string

content

[].title

string

formatted name of the commented element

[].pinned

boolean

should the comment be visible to everybody on the map

[].removed

boolean

is the comment removed

[].removeReason

string

reason why comment was removed

[].id

integer

comment identifier

[].modelId

integer

map identifier

[].coord

point

coordinates where comment should be pinned

[].icon

string

icon that should be used to visualize this comment

[].elementId

string

element identifier

[].type

string

type of the element that was commented on. Available options ALIAS, POINT, REACTION

2.5. Sample Response
[ {
  "title" : "Reaction path_0_re5933",
  "icon" : "icons/comment.png?v=Unknown",
  "type" : "REACTION",
  "content" : null,
  "removed" : false,
  "coord" : {
    "x" : 5.0,
    "y" : 0.0
  },
  "modelId" : 311,
  "elementId" : "159",
  "id" : 55,
  "pinned" : false,
  "email" : null,
  "owner" : null,
  "removeReason" : ""
} ]
3. Get comments for specific element
3.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/comments/models/355/bioEntities/elements/890' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
3.2. Path Parameters
Table 3. /minerva/api/projects/{projectId}/comments/models/{mapId}/bioEntities/elements/{elementId}
Parameter	Description
projectId

project identifier

mapId

map identifier

elementId

element identifier

3.3. Request Parameters
Parameter	Description
columns

set of columns (all by default). Available options: title, icon, type, content, removed, coord, modelId, elementId, id, pinned, email, owner, removeReason

removed

true/false/undefined - when defined comment property must match this parameter

3.4. Response Fields
Path	Type	Description
[]

array<Comment>

list of comments

[].owner

string

login of the user that created a comment

[].email

string

author email address

[].content

string

content

[].title

string

formatted name of the commented element

[].pinned

boolean

should the comment be visible to everybody on the map

[].removed

boolean

is the comment removed

[].removeReason

string

reason why comment was removed

[].id

integer

comment identifier

[].modelId

integer

map identifier

[].coord

point

coordinates where comment should be pinned

[].icon

string

icon that should be used to visualize this comment

[].elementId

string

element identifier

[].type

string

type of the element that was commented on. Available options ALIAS, POINT, REACTION

3.5. Sample Response
[ {
  "title" : "water",
  "icon" : "icons/comment.png?v=Unknown",
  "type" : "ALIAS",
  "content" : null,
  "removed" : false,
  "coord" : {
    "x" : 60.0,
    "y" : 30.0
  },
  "modelId" : 355,
  "elementId" : "890",
  "id" : 75,
  "pinned" : false,
  "email" : null,
  "owner" : null,
  "removeReason" : ""
} ]
4. Get comments for specific point
4.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/comments/models/323/points/10.00,20.00' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
4.2. Path Parameters
Table 4. /minerva/api/projects/{projectId}/comments/models/{mapId}/points/{point}
Parameter	Description
projectId

project identifier

mapId

map identifier

point

point coordinates

4.3. Request Parameters
Parameter	Description
columns

set of columns (all by default). Available options: title, icon, type, content, removed, coord, modelId, elementId, id, pinned, email, owner, removeReason

removed

true/false/undefined - when defined comment property must match this parameter

4.4. Response Fields
Path	Type	Description
[]

array<Comment>

list of comments

[].owner

string

login of the user that created a comment

[].email

string

author email address

[].content

string

content

[].title

string

formatted name of the commented element

[].pinned

boolean

should the comment be visible to everybody on the map

[].removed

boolean

is the comment removed

[].removeReason

string

reason why comment was removed

[].id

integer

comment identifier

[].modelId

integer

map identifier

[].coord

point

coordinates where comment should be pinned

[].icon

string

icon that should be used to visualize this comment

[].elementId

string

element identifier

[].type

string

type of the element that was commented on. Available options ALIAS, POINT, REACTION

4.5. Sample Response
[ {
  "title" : "Comment (coord: 10.00, 20.00)",
  "icon" : "icons/comment.png?v=Unknown",
  "type" : "POINT",
  "content" : null,
  "removed" : false,
  "coord" : {
    "x" : 10.0,
    "y" : 20.0
  },
  "modelId" : 323,
  "elementId" : "10.00,20.00",
  "id" : 60,
  "pinned" : false,
  "email" : null,
  "owner" : null,
  "removeReason" : ""
} ]
5. Create element comment
5.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/comments/models/315/bioEntities/elements/787' -X POST \
    -d 'email=a%40a.lu&content=test+content&pinned=true&coordinates=10%2C2&modelId=315' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
5.2. Path Parameters
Table 5. /minerva/api/projects/{projectId}/comments/models/{mapId}/bioEntities/elements/{elementId}
Parameter	Description
projectId

project identifier

mapId

map identifier

elementId

element identifier

5.3. Request Parameters
Parameter	Description
modelId

map identifier

content

content

email

user email address

coordinates

coordinates where comment should be pinned

pinned

should the comment be visible to everybody

5.4. Response Fields
Path	Type	Description
owner

string

login of the user that created a comment

email

string

author email address

content

string

content

title

string

formatted name of the commented element

pinned

boolean

should the comment be visible to everybody on the map

removed

boolean

is the comment removed

removeReason

string

reason why comment was removed

id

integer

comment identifier

modelId

integer

map identifier

coord

point

coordinates where comment should be pinned

icon

string

icon that should be used to visualize this comment

elementId

string

element identifier

type

string

type of the element that was commented on. Available options ALIAS, POINT, REACTION

5.5. Sample Response
{
  "title" : "Comp",
  "icon" : "icons/comment.png?v=Unknown",
  "type" : "ALIAS",
  "content" : "test content",
  "removed" : false,
  "coord" : {
    "x" : 505.0,
    "y" : 505.0
  },
  "modelId" : 315,
  "elementId" : "787",
  "id" : 57,
  "pinned" : true,
  "email" : "a@a.lu",
  "owner" : "test_user",
  "removeReason" : ""
}
6. Create reaction comment
6.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/comments/models/385/bioEntities/reactions/196' -X POST \
    -d 'email=a%40a.lu&content=test+content&pinned=true&coordinates=10%2C2&modelId=385' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
6.2. Path Parameters
Table 6. /minerva/api/projects/{projectId}/comments/models/{mapId}/bioEntities/reactions/{reactionId}
Parameter	Description
projectId

project identifier

mapId

map identifier

reactionId

reaction identifier

6.3. Request Parameters
Parameter	Description
modelId

map identifier

content

content

email

user email address

coordinates

coordinates where comment should be pinned

pinned

should the comment be visible to everybody

6.4. Response Fields
Path	Type	Description
owner

string

login of the user that created a comment

email

string

author email address

content

string

content

title

string

formatted name of the commented element

pinned

boolean

should the comment be visible to everybody on the map

removed

boolean

is the comment removed

removeReason

string

reason why comment was removed

id

integer

comment identifier

modelId

integer

map identifier

coord

point

coordinates where comment should be pinned

icon

string

icon that should be used to visualize this comment

elementId

string

element identifier

type

string

type of the element that was commented on. Available options ALIAS, POINT, REACTION

6.5. Sample Response
{
  "title" : "Reaction path_0_re5933",
  "icon" : "icons/comment.png?v=Unknown",
  "type" : "REACTION",
  "content" : "test content",
  "removed" : false,
  "coord" : {
    "x" : 5.0,
    "y" : 0.0
  },
  "modelId" : 385,
  "elementId" : "196",
  "id" : 96,
  "pinned" : true,
  "email" : "a@a.lu",
  "owner" : "test_user",
  "removeReason" : ""
}
7. Create coordinates comment
7.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/comments/models/375/points/10,2' -X POST \
    -d 'email=a%40a.lu&content=test+content&pinned=true&modelId=375' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
7.2. Path Parameters
Table 7. /minerva/api/projects/{projectId}/comments/models/{mapId}/points/{point}
Parameter	Description
projectId

project identifier

mapId

map identifier

point

point coordinates

7.3. Request Parameters
Parameter	Description
modelId

map identifier

content

content

email

user email address

coordinates

coordinates where comment should be pinned

pinned

should the comment be visible to everybody

7.4. Response Fields
Path	Type	Description
owner

string

login of the user that created a comment

email

string

author email address

content

string

content

title

string

formatted name of the commented element

pinned

boolean

should the comment be visible to everybody on the map

removed

boolean

is the comment removed

removeReason

string

reason why comment was removed

id

integer

comment identifier

modelId

integer

map identifier

coord

point

coordinates where comment should be pinned

icon

string

icon that should be used to visualize this comment

elementId

string

element identifier

type

string

type of the element that was commented on. Available options ALIAS, POINT, REACTION

7.5. Sample Response
{
  "title" : "Comment (coord: 10.00, 2.00)",
  "icon" : "icons/comment.png?v=Unknown",
  "type" : "POINT",
  "content" : "test content",
  "removed" : false,
  "coord" : {
    "x" : 10.0,
    "y" : 2.0
  },
  "modelId" : 375,
  "elementId" : "10.00,2.00",
  "id" : 87,
  "pinned" : true,
  "email" : "a@a.lu",
  "owner" : "test_user",
  "removeReason" : ""
}
8. Delete comment
8.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/comments/50/' -X DELETE \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
8.2. Path Parameters
Table 8. /minerva/api/projects/{projectId}/comments/{commentId}/
Parameter	Description
projectId

project identifier

commentId

comment identifier


1. Get drug
Returns drugs data with project related connections.

1.1. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/drugs:search?query=aspirin' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.2. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/Some_id/drugs:search?target=ALIAS:993' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.3. Path Parameters
Table 1. /minerva/api/projects/{projectId}/drugs:search
Parameter	Description
projectId

project identifier

1.4. Request Parameters
Parameter	Description
columns

set of columns (all by default). Available options: name, references, description, synonyms, id, directEvidenceReferences, directEvidence, targets

query

name of chemical that we are searching for

target

target element that we are searching for in format TYPE:ID

1.5. Response Fields
Path	Type	Description
[].id

object

identifier of the chemical

[].name

string

name

[].description

string

description

[].synonyms

array<string>

list of synonyms

[].brandNames

array<string>

list of brand names

[].bloodBrainBarrier

string

does drug cross blood brain barrier

[].references

array<Reference>

list of references

[].targets

array<Target>

list of targets

[].targets[].name

string

target name

[].targets[].references

array<Reference>

list of target references

[].targets[].targetElements

array<object>

list of elements on the map associated with this target

[].targets[].targetParticipants

array<object>

list of identifiers associated with this target

1.6. Sample Response
[ {
  "name" : "ASPIRIN",
  "references" : [ {
    "link" : "https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL25",
    "type" : "CHEMBL_COMPOUND",
    "resource" : "CHEMBL25",
    "id" : 0,
    "annotatorClassName" : ""
  } ],
  "description" : null,
  "bloodBrainBarrier" : "N/A",
  "brandNames" : [ ],
  "synonyms" : [ "8-HOUR BAYER", "Acetosalic Acid", "ACETYLSALIC ACID", "ACETYL SALICYLATE", "Acetylsalicylic Acid", "Acetylsalicylic Acid", "ACETYLSALICYLIC ACID", "ACETYLSALICYLIC ACID", "ACETYLSALICYLIC ACID (WHO-IP)", "ACETYLSALICYLICUM ACIDUM", "ACIDUM ACETYLSALICYLICUM", "ACIDUM ACETYLSALICYLICUM (WHO-IP)", "ALKA RAPID", "ANADIN ALL NIGHT", "ANGETTES 75", "Aspirin", "ASPIRIN", "ASPIRIN", "ASPIRIN", "ASPIRIN", "ASPIRIN", "ASPIRIN", "ASPIRIN", "ASPIRIN", "ASPRO CLR", "BAY1019036", "BAYER EXTRA STRENGTH ASPIRIN FOR MIGRAINE PAIN", "BENZOIC ACID, 2-(ACETYLOXY)-", "DANAMEP", "DISPRIN CV", "DISPRIN DIRECT", "DURLAZA", "Ecotrin", "ENPRIN", "Equi-Prin", "GENCARDIA", "LEVIUS", "MAX STRGH ASPRO CLR", "MEASURIN", "MICROPIRIN EC", "NSC-27223", "NSC-406186", "NU-SEALS 300", "NU-SEALS 600", "NU-SEALS 75", "NU-SEALS CARDIO 75", "PAYNOCIL", "PLATET", "PLATET 300", "POSTMI 300", "POSTMI 75", "Salicylic Acid Acetate", "VAZALORE" ],
  "id" : "ASPIRIN",
  "targets" : [ {
    "name" : "Cyclooxygenase",
    "targetParticipants" : [ {
      "link" : "https://www.genenames.org/data/gene-symbol-report/#!/symbol/PTGS2",
      "type" : "HGNC_SYMBOL",
      "resource" : "PTGS2",
      "id" : 0,
      "annotatorClassName" : ""
    }, {
      "link" : "https://www.genenames.org/data/gene-symbol-report/#!/symbol/PTGS1",
      "type" : "HGNC_SYMBOL",
      "resource" : "PTGS1",
      "id" : 0,
      "annotatorClassName" : ""
    } ],
    "references" : [ {
      "link" : "https://pubmed.ncbi.nlm.nih.gov/17258197/",
      "article" : null,
      "type" : "PUBMED",
      "resource" : "17258197",
      "id" : 0,
      "annotatorClassName" : ""
    }, {
      "link" : "https://pubmed.ncbi.nlm.nih.gov/17131625/",
      "article" : null,
      "type" : "PUBMED",
      "resource" : "17131625",
      "id" : 0,
      "annotatorClassName" : ""
    } ],
    "targetElements" : [ ]
  } ]
} ]
2. Get suggested drug queries
Get list of suggested drug queries in the context of the project.

2.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/drugs/suggestedQueryList' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
2.2. Path Parameters
Table 2. /minerva/api/projects/{projectId}/drugs/suggestedQueryList
Parameter	Description
projectId

project identifier

2.3. Response Fields
Path	Type	Description
[]

array<string>

list of suggested drug queries

2.4. Sample Response
[ ]

1. List maps
List all (sub)maps in a project.

1.1. Path Parameters
Table 1. /minerva/api/projects/{projectId}/models/
Parameter	Description
projectId

project identifier

1.2. Response Fields
Path	Type	Description
[]

array<Map>

list of maps

1.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/empty/models/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.4. Sample Response
[ {
  "idObject" : 3,
  "width" : 25195.0,
  "height" : 14285.0,
  "defaultCenterX" : null,
  "defaultCenterY" : null,
  "description" : "",
  "name" : "",
  "defaultZoomLevel" : null,
  "tileSize" : 256,
  "references" : [ ],
  "authors" : [ ],
  "creationDate" : null,
  "modificationDates" : [ ],
  "minZoom" : 2,
  "maxZoom" : 9
} ]
2. Get by id
Returns map identified by id.

2.1. Path Parameters
Table 2. /minerva/api/projects/{projectId}/models/{mapId}
Parameter	Description
projectId

project identifier

mapId

map identifier

2.2. Response Fields
Path	Type	Description
name

string

name of the map

description

string

description

idObject

number

map id

width

number

map width

height

number

map height

tileSize

number

size of the png tile used to visualize in frontend

defaultCenterX

number

default x center used in frontend visualization

defaultCenterY

number

default y center used in frontend visualization

defaultZoomLevel

number

default zoom level used in frontend visualization

minZoom

number

minimum zoom level available for the map

maxZoom

number

maximum zoom level available for the map

authors

array<Author>

list of authors

references

array<Reference>

list of references

creationDate

timestamp

creation date

modificationDates

array<timestamp>

modification dates

2.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/486' -X GET
2.4. Sample Response
{
  "idObject" : 486,
  "width" : 100.0,
  "height" : 100.0,
  "defaultCenterX" : null,
  "defaultCenterY" : null,
  "description" : "",
  "name" : "Unknown",
  "defaultZoomLevel" : null,
  "tileSize" : 256,
  "references" : [ ],
  "authors" : [ ],
  "creationDate" : null,
  "modificationDates" : [ ],
  "minZoom" : 2,
  "maxZoom" : 2
}
3. Update map
Updates map data.

3.1. Path Parameters
Table 3. /minerva/api/projects/{projectId}/models/{mapId}
Parameter	Description
projectId

project identifier

mapId

map identifier

3.2. Request Fields
Path	Type	Description
model.defaultCenterX

Number

default x center used in frontend visualization

model.defaultCenterY

Number

default y center used in frontend visualization

model.defaultZoomLevel

Number

default zoom level used in frontend visualization

3.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/427' -X PATCH \
    -d '{"model":{"defaultZoomLevel":3,"defaultCenterY":20.0,"defaultCenterX":10.0}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
3.4. Sample Response
{
  "idObject" : 427,
  "width" : 400.0,
  "height" : 400.0,
  "defaultCenterX" : 10.0,
  "defaultCenterY" : 20.0,
  "description" : "",
  "name" : "map_name",
  "defaultZoomLevel" : 3,
  "tileSize" : 256,
  "references" : [ ],
  "authors" : [ ],
  "creationDate" : null,
  "modificationDates" : [ ],
  "minZoom" : 2,
  "maxZoom" : 2
}
4. Get connections between maps
Returns list of connections between (sub)maps in a project.

4.1. Path Parameters
Table 4. /minerva/api/projects/{projectId}/submapConnections/
Parameter	Description
projectId

project identifier

4.2. Response Fields
Path	Type	Description
[]

Array

list of connections

[].from.id

Number

anchor bioEntity id

[].from.modelId

Number

anchor map id

[].from.type

String

anchor type

[].to.modelId

Number

destination map id

4.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/submapConnections/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
4.4. Sample Response
[ {
  "from" : {
    "id" : 1896,
    "modelId" : 765,
    "type" : "ALIAS"
  },
  "to" : {
    "modelId" : 766
  }
} ]
5. Download map
Download map in a standard format.

5.1. Path Parameters
Table 5. /minerva/api/projects/{projectId}/models/{mapId}:downloadModel
Parameter	Description
projectId

project identifier

mapId

map identifier

5.2. Request Parameters
Parameter	Description
handlerClass

class preparing model file. Available options: lcsb.mapviewer.converter.model.celldesigner.CellDesignerXmlParser, lcsb.mapviewer.converter.model.sbgnml.SbgnmlXmlConverter, lcsb.mapviewer.converter.model.sbml.SbmlParser, lcsb.mapviewer.wikipathway.GpmlParser

polygonString

polygon defining part of the model to be downloaded

strictCutoff

must the reactions be inside polygon (default: true)

elementIds

list of element ids that should be included in the output

reactionIds

list of reaction ids that should be included in the output

5.3. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/488:downloadModel?handlerClass=lcsb.mapviewer.converter.model.celldesigner.CellDesignerXmlParser' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
5.4. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/487:downloadModel?handlerClass=lcsb.mapviewer.converter.model.celldesigner.CellDesignerXmlParser&polygonString=0,0;100,0;0,100&strictCutoff=false' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
5.5. CURL sample 3
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/481:downloadModel?handlerClass=lcsb.mapviewer.converter.model.celldesigner.CellDesignerXmlParser&elementIds=1202' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
6. Download map as image
Download map as image.

6.1. Path Parameters
Table 6. /minerva/api/projects/{projectId}/models/{mapId}:downloadImage
Parameter	Description
projectId

project identifier

mapId

map identifier

6.2. Request Parameters
Parameter	Description
handlerClass

class preparing image. Available options: lcsb.mapviewer.converter.graphics.PngImageGenerator, lcsb.mapviewer.converter.graphics.PdfImageGenerator, lcsb.mapviewer.converter.graphics.SvgImageGenerator

polygonString

polygon defining part of the map to be downloaded

backgroundOverlayId

identifier of the overlay used as a background when creating image

zoomLevel

zoom level at which image should be generated (min value used by default)

overlayIds

comma separated list of overlay identifiers that should be included in the image

6.3. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/477:downloadImage?handlerClass=lcsb.mapviewer.converter.graphics.PngImageGenerator' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
6.4. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/465:downloadImage?handlerClass=lcsb.mapviewer.converter.graphics.PdfImageGenerator&polygonString=0,0;100,0;100,100;0,100' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
7. Get elements
Get list of elements.

7.1. Path Parameters
Table 7. /minerva/api/projects/{projectId}/models/{mapId}/bioEntities/elements/
Parameter	Description
projectId

project identifier

mapId

map identifier

7.2. Request Parameters
Parameter	Description
id

set of database ids (all by default)

columns

set of columns (all by default). Available options: id, elementId, modelId, name, type, notes, symbol, complexId, compartmentId, fullName, abbreviation, formula, synonyms, formerSymbols, references, bounds, hierarchyVisibilityLevel, transparencyLevel, linkedSubmodel, other, initialConcentration, boundaryCondition, immediateLink, constant, hypothetical, activity, initialAmount, glyph, homomultimer

includedCompartmentIds

set of database compartment ids (all by default)

excludedCompartmentIds

set of database compartment ids (none by default)

type

element type (all by default). Available options: Antisense RNA, Compartment, Complex, Degraded, Drug, Gene, Ion, Pathway, Phenotype, Protein, RNA, Simple molecule, Unknown

7.3. Response Fields
Path	Type	Description
[].id

number

unique element identifier

[].elementId

string

element identifier taken from source file

[].name

string

name

[].immediateLink

String

link that should be opened immediately when element is clicked on the map

[].modelId

number

map identifier

[].complexId

number

identifier of a complex in which element is located

[].compartmentId

number

identifier of a compartment in which element is located

[].linkedSubmodel

number

identifier of a submap to which this element is an entry point (anchor)

[].type

string

element type

[].bounds

object

coordinates and the dimension of the element on the map

[].hierarchyVisibilityLevel

string

at what zoom level this element becomes visible in hierarchical view

[].transparencyLevel

string

at what zoom level this element becomes transparent in hierarchical view

[].synonyms

array<string>

list of synonyms

[].formerSymbols

array<string>

list of former symbols

[].references

array<Reference>

list of references

[].notes

string

notes and description

[].symbol

string

symbol

[].fullName

string

full name

[].abbreviation

string

abbreviation

[].formula

string

formula

[].boundaryCondition

boolean

SBML kinetics is boundary condition

[].constant

boolean

SBML kinetics is constant

[].initialAmount

number

SBML kinetics initial amount

[].initialConcentration

boolean

SBML kinetics initial concentration

[].glyph

Glyph

image glyph associated with the element

[].glyph.fileId

Glyph

id of file associated with the glyph

[].activity

boolean

is the element active

[].hypothetical

boolean

is the element hypothetical

[].homomultimer

int

multimer value

[].other

object

list of other properties

7.4. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/bioEntities/elements/' -X GET
7.5. Sample Response 1
[ {
  "abbreviation" : null,
  "activity" : false,
  "boundaryCondition" : false,
  "bounds" : {
    "height" : 20.0,
    "width" : 100.0,
    "x" : 10.0,
    "y" : 20.0,
    "z" : 10
  },
  "compartmentId" : null,
  "complexId" : null,
  "constant" : false,
  "elementId" : "p1",
  "formerSymbols" : [ ],
  "formula" : null,
  "fullName" : null,
  "glyph" : {
    "fileId" : 275
  },
  "hierarchyVisibilityLevel" : "",
  "homomultimer" : 1,
  "hypothetical" : false,
  "id" : 1203,
  "immediateLink" : null,
  "initialAmount" : null,
  "initialConcentration" : 0.0,
  "linkedSubmodel" : null,
  "modelId" : 482,
  "name" : "GSTA4",
  "notes" : "",
  "other" : {
    "modifications" : [ {
      "modificationId" : "r2",
      "name" : "",
      "type" : "RESIDUE"
    } ],
    "structuralState" : "",
    "structures" : { }
  },
  "references" : [ ],
  "symbol" : null,
  "synonyms" : [ "GSTA_XX", "GSTA_YY" ],
  "transparencyLevel" : "",
  "type" : "Protein"
} ]
7.6. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/bioEntities/elements/?columns=name,complexId&type=Protein' -X GET
8. Get reactions
Get list of reactions.

8.1. Path Parameters
Table 8. /minerva/api/projects/{projectId}/models/{mapId}/bioEntities/reactions/
Parameter	Description
projectId

project identifier

mapId

map identifier

8.2. Request Parameters
Parameter	Description
id

set of database ids (all by default)

columns

set of columns (all by default). Available options: id, reactionId, modelId, type, name, lines, kineticLaw, centerPoint, products, reactants, modifiers, hierarchyVisibilityLevel, references, notes

participantId

set of element identifiers for which reaction we are looking for (only reactions with at least one participant will be returned)

8.3. Response Fields
Path	Type	Description
[].id

Number

unique element identifier

[].reactionId

String

reaction identifier taken from source file

[].name

String

reaction name

[].modelId

Number

map identifier

[].type

String

reaction type

[].centerPoint

Object

center point

[].lines

Array

list of lines used to draw reaction

[].hierarchyVisibilityLevel

String

at what zoom level this element becomes visible in hierarchical view

[].references

Array

list of references

[].modifiers

Array

list of modifiers

[].reactants

Array

list of reactants

[].products

Array

list of products

[].notes

String

notes and description

[].kineticLaw

Object

SBML kinetics law

[].other

Object

list of other properties

[].reactants[].aliasId

Number

element identifier

[].reactants[].type

String

type

[].reactants[].stoichiometry

String

element stoichiometry

[].products[].aliasId

Number

element identifier

[].products[].type

String

type

[].products[].stoichiometry

String

element stoichiometry

[].modifiers[].aliasId

Number

element identifier

[].modifiers[].type

String

type

[].modifiers[].stoichiometry

String

element stoichiometry

8.4. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/bioEntities/reactions/' -X GET
8.5. Sample Response 1
[ {
  "centerPoint" : {
    "x" : 5.0,
    "y" : 0.0
  },
  "hierarchyVisibilityLevel" : "",
  "id" : 238,
  "kineticLaw" : {
    "definition" : "<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><lambda>\n<bvar>\n<ci> x </ci>\n</bvar>\n<bvar>\n<ci> y </ci>\n</bvar>\n<apply>\n<plus/>\n<ci> x </ci>\n<ci> y </ci>\n</apply>\n</lambda></math>",
    "functionIds" : [ ],
    "mathMlPresentation" : "\n<math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n   <mrow>\n      <mo>λ</mo>\n      <mrow>\n         <mo>(</mo>\n         <mi> x </mi>\n         <mo>,</mo>\n         <mi> y </mi>\n         <mo>,</mo>\n         <mrow>\n            <mi> x </mi>\n            <mo>+</mo>\n            <mi> y </mi>\n         </mrow>\n         <mo>)</mo>\n      </mrow>\n   </mrow>\n</math>\n",
    "parameterIds" : [ ]
  },
  "lines" : [ {
    "start" : {
      "x" : 10.0,
      "y" : 0.0
    },
    "end" : {
      "x" : 0.0,
      "y" : 0.0
    },
    "type" : "START"
  }, {
    "start" : {
      "x" : 15.0,
      "y" : 0.0
    },
    "end" : {
      "x" : 20.0,
      "y" : 0.0
    },
    "type" : "END"
  }, {
    "start" : {
      "x" : 15.0,
      "y" : 0.0
    },
    "end" : {
      "x" : 30.0,
      "y" : 0.0
    },
    "type" : "END"
  }, {
    "start" : {
      "x" : 10.0,
      "y" : 0.0
    },
    "end" : {
      "x" : 15.0,
      "y" : 0.0
    },
    "type" : "MIDDLE"
  }, {
    "start" : {
      "x" : 0.0,
      "y" : 0.0
    },
    "end" : {
      "x" : 10.0,
      "y" : 0.0
    },
    "type" : "MIDDLE"
  } ],
  "modelId" : 469,
  "modifiers" : [ ],
  "name" : "",
  "notes" : "",
  "products" : [ {
    "aliasId" : 1173,
    "stoichiometry" : null,
    "type" : "Product"
  }, {
    "aliasId" : 1176,
    "stoichiometry" : null,
    "type" : "Product"
  } ],
  "reactants" : [ {
    "aliasId" : 1173,
    "stoichiometry" : null,
    "type" : "Reactant"
  } ],
  "reactionId" : "path_0_re5933",
  "references" : [ {
    "link" : null,
    "article" : null,
    "type" : "PUBMED",
    "resource" : "28725475",
    "id" : 1374,
    "annotatorClassName" : ""
  }, {
    "link" : null,
    "article" : null,
    "type" : "PUBMED",
    "resource" : "invalid123",
    "id" : 1375,
    "annotatorClassName" : ""
  } ],
  "type" : "Transport"
} ]
8.6. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/bioEntities/reactions/?columns=id,notes' -X GET
9. Search for bio entities
Returns list of bio entities matching the query.

9.1. Path Parameters
Table 9. /minerva/api/projects/{projectId}/models/{mapId}/bioEntities:search
Parameter	Description
projectId

project identifier

mapId

map identifier

9.2. Request Parameters
Parameter	Description
query

search term identifying bioEntity

coordinates

coordinates where bioEntity should be located

count

max number of bioEntities to return

type

type of bioEntity, available values are: antisense rna, catalysis, compartment, complex, degraded, dissociation, drug, gene, heterodimer association, inhibition, ion, known transition omitted, modulation, negative influence, pathway, phenotype, physical stimulation, positive influence, protein, reduced modulation, reduced physical stimulation, reduced trigger, rna, simple molecule, state transition, transcription, translation, transport, trigger, truncation, unknown, unknown catalysis, unknown inhibition, unknown negative influence, unknown positive influence, unknown reduced modulation, unknown reduced physical stimulation, unknown reduced trigger, unknown transition

perfectMatch

true when true query must be matched exactly, if false similar results are also acceptable

9.3. Response Fields
Path	Type	Description
[].id

number

unique element identifier

[].modelId

number

map identifier

[].type

string

type of the bioEntity (available options: ALIAS, REACTION)

9.4. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/bioEntities:search?query=p2' -X GET
9.5. Sample Response 1
[ {
  "id" : 1140,
  "modelId" : 455,
  "type" : "ALIAS"
} ]
9.6. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/409/bioEntities:search?coordinates=104.36,182.81' -X GET
10. Get list of suggested search queries
10.1. Path Parameters
Table 10. /minerva/api/projects/{projectId}/models/{mapId}/bioEntities/suggestedQueryList
Parameter	Description
projectId

project identifier

mapId

map identifier

10.2. Response Fields
Path	Type	Description
[]

array<string>

list of all full search queries that could be used for querying the map

10.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/bioEntities/suggestedQueryList' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
10.4. Sample Response
[ "comp", "gsta4", "gsta_xx", "gsta_yy", "water" ]
11. Kinetic functions
Get list of kinetic functions.

11.1. Path Parameters
Table 11. /minerva/api/projects/{projectId}/models/{mapId}/functions/
Parameter	Description
projectId

project identifier

mapId

map identifier

11.2. Response Fields
Path	Type	Description
[]

Array

list of functions

[].id

Number

unique function identifier

[].name

String

name

[].definition

String

definition

[].mathMlPresentation

String

mathMl representation of the definition

[].functionId

String

function identifier taken from source file

[].arguments

Array

list of function parameters

11.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/405/functions/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
11.4. Sample Response
[ {
  "id" : 385,
  "functionId" : "f1",
  "name" : "name",
  "definition" : "<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><lambda>\n<bvar>\n<ci> x </ci>\n</bvar>\n<bvar>\n<ci> y </ci>\n</bvar>\n<apply>\n<plus/>\n<ci> x </ci>\n<ci> y </ci>\n</apply>\n</lambda></math>",
  "arguments" : [ ],
  "mathMlPresentation" : "\n<math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n   <mrow>\n      <mi> x </mi>\n      <mo>+</mo>\n      <mi> y </mi>\n   </mrow>\n</math>\n"
} ]
12. Kinetic function
Get information about specific kinetic function.

12.1. Path Parameters
Table 12. /minerva/api/projects/{projectId}/models/{mapId}/functions/{functionId}
Parameter	Description
projectId

project identifier

mapId

map identifier

functionId

function identifier

12.2. Response Fields
Path	Type	Description
id

Number

unique function identifier

name

String

name

definition

String

definition

mathMlPresentation

String

mathMl representation of the definition

functionId

String

function identifier taken from source file

arguments

Array

list of function parameters

12.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/403/functions/383' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
12.4. Sample Response
{
  "id" : 383,
  "functionId" : "f1",
  "name" : "name",
  "definition" : "<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><lambda>\n<bvar>\n<ci> x </ci>\n</bvar>\n<bvar>\n<ci> y </ci>\n</bvar>\n<apply>\n<plus/>\n<ci> x </ci>\n<ci> y </ci>\n</apply>\n</lambda></math>",
  "arguments" : [ ],
  "mathMlPresentation" : "\n<math xmlns=\"http://www.w3.org/1998/Math/MathML\">\n   <mrow>\n      <mi> x </mi>\n      <mo>+</mo>\n      <mi> y </mi>\n   </mrow>\n</math>\n"
}
13. Kinetic parameters
Get list of kinetic parameters.

13.1. Path Parameters
Table 13. /minerva/api/projects/{projectId}/models/{mapId}/parameters/
Parameter	Description
projectId

project identifier

mapId

map identifier

13.2. Response Fields
Path	Type	Description
[]

Array

list of parameters

[].id

number

unique parameter identifier

[].name

string

name

[].value

number

value

[].unitsId

number

unit identifier

[].global

boolean

is parameter global

[].parameterId

string

parameter identifier taken from source file

13.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/parameters/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
13.4. Sample Response
[ {
  "global" : true,
  "id" : 347,
  "name" : "D coefficient",
  "parameterId" : "parameter1",
  "unitsId" : null,
  "value" : 1.0
} ]
14. Kinetic parameter
Get information about specific kinetic parameter.

14.1. Path Parameters
Table 14. /minerva/api/projects/{projectId}/models/{mapId}/parameters/{parameterId}
Parameter	Description
projectId

project identifier

mapId

map identifier

parameterId

parameter identifier

14.2. Response Fields
Path	Type	Description
id

number

unique parameter identifier

name

string

name

value

number

value

unitsId

number

unit identifier

global

boolean

is parameter global

parameterId

string

parameter identifier taken from source file

14.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/parameters/345' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
14.4. Sample Response
{
  "global" : true,
  "id" : 345,
  "name" : "D coefficient",
  "parameterId" : "parameter1",
  "unitsId" : null,
  "value" : 1.0
}
15. Get units
Get list of units.

15.1. Path Parameters
Table 15. /minerva/api/projects/{projectId}/models/{mapId}/units/
Parameter	Description
projectId

project identifier

mapId

map identifier

15.2. Response Fields
Path	Type	Description
[]

Array

list of units

[].id

number

unique unit identifier

[].name

string

name

[].unitTypeFactors

array<object>

in complex unit this define how specific unit types are associated

[].unitId

string

unit identifier taken from source file

15.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/units/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
15.4. Sample Response
[ {
  "id" : 717,
  "unitId" : "u1",
  "name" : "Weight",
  "unitTypeFactors" : [ ]
} ]
16. Get unit
Get information about specific unit.

16.1. Path Parameters
Table 16. /minerva/api/projects/{projectId}/models/{mapId}/units/{unitId}
Parameter	Description
projectId

project identifier

mapId

map identifier

unitId

unit identifier

16.2. Response Fields
Path	Type	Description
id

number

unique unit identifier

name

string

name

unitTypeFactors

array<object>

in complex unit this define how specific unit types are associated

unitId

string

unit identifier taken from source file

16.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/models/*/units/718' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
16.4. Sample Response
{
  "id" : 718,
  "unitId" : "u1",
  "name" : "Weight",
  "unitTypeFactors" : [ ]
}
1. Get miRNA
Returns miRNAs data with project related connections.

1.1. CURL sample
Unresolved directive in project_mirna.adoc - include::../../../target/generated-snippets/projects/project_mirna/search_by_query/curl-request.adoc[]

1.2. Path Parameters
Unresolved directive in project_mirna.adoc - include::../../../target/generated-snippets/projects/project_mirna/search_by_query/path-parameters.adoc[]

1.3. Response Fields
Unresolved directive in project_mirna.adoc - include::../../../target/generated-snippets/projects/project_mirna/search_by_query/response-fields.adoc[]

1.4. Sample Response
Unresolved directive in project_mirna.adoc - include::../../../target/generated-snippets/projects/project_mirna/search_by_query/response-body.adoc[]

2. Get suggested miRNA queries
Get list of suggested miRNA queries in the context of the project.

2.1. CURL sample
Unresolved directive in project_mirna.adoc - include::../../../target/generated-snippets/projects/project_mirna/suggested_query_list/curl-request.adoc[]

2.2. Path Parameters
Unresolved directive in project_mirna.adoc - include::../../../target/generated-snippets/projects/project_mirna/suggested_query_list/path-parameters.adoc[]

2.3. Response Fields
Unresolved directive in project_mirna.adoc - include::../../../target/generated-snippets/projects/project_mirna/suggested_query_list/response-fields.adoc[]

2.4. Sample Response
Unresolved directive in project_mirna.adoc - include::../../../target/generated-snippets/projects/project_mirna/suggested_query_list/response-body.adoc[]

1. List data overlays
1.1. Path Parameters
Table 1. /minerva/api/projects/{projectId}/overlays/
Parameter	Description
projectId

project identifier

1.2. Response Fields
Path	Type	Description
[].name

String

name

[].description

String

description

[].idObject

Number

identifier

[].publicOverlay

Boolean

is the data overlay publicly available to all users

[].order

Number

sort order

[].type

String

type; available options: GENERIC, GENETIC_VARIANT

[].genomeType

String

reference genome type; available options: UCSC

[].genomeVersion

String

reference genome version

[].creator

String

login of the user who uploaded data overlay

1.3. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.4. Sample Response 1
[ {
  "name" : "test title",
  "creator" : "admin",
  "description" : "test description",
  "genomeType" : null,
  "genomeVersion" : null,
  "idObject" : 1000137,
  "publicOverlay" : true,
  "type" : "GENERIC",
  "order" : 0
}, {
  "name" : "test title",
  "creator" : "test_user",
  "description" : "test description",
  "genomeType" : null,
  "genomeVersion" : null,
  "idObject" : 1000138,
  "publicOverlay" : false,
  "type" : "GENERIC",
  "order" : 0
} ]
1.5. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/?creator=test_curator' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.6. Sample Response 2
[ {
  "name" : "test title",
  "creator" : "test_curator",
  "description" : "test description",
  "genomeType" : null,
  "genomeVersion" : null,
  "idObject" : 1000148,
  "publicOverlay" : false,
  "type" : "GENERIC",
  "order" : 0
} ]
2. Get data overlay
2.1. Path Parameters
Table 2. /minerva/api/projects/{projectId}/overlays/{overlayId}/
Parameter	Description
projectId

project identifier

overlayId

overlay identifier

2.2. Response Fields
Path	Type	Description
name

String

name

description

String

description

idObject

Number

identifier

publicOverlay

Boolean

is the data overlay publicly available to all users

order

Number

sort order

type

String

type; available options: GENERIC, GENETIC_VARIANT

genomeType

String

reference genome type; available options: UCSC

genomeVersion

String

reference genome version

creator

String

login of the user who uploaded data overlay

2.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/1000110/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
2.4. Sample Response
{
  "name" : "test title",
  "creator" : "test_user",
  "description" : "test description",
  "genomeType" : null,
  "genomeVersion" : null,
  "idObject" : 1000110,
  "publicOverlay" : false,
  "type" : "GENERIC",
  "order" : 0
}
3. Add overlay
3.1. Path Parameters
Table 3. /minerva/api/projects/{projectId}/overlays/
Parameter	Description
projectId

project identifier

3.2. Request Parameters
Parameter	Description
name

name of the data overlay

content

content of the file that is uploaded with definition what should be visible where (alternative to fileId)

fileId

uploaded file id that should be used as data overlay content content (alternative to content)

description

short description of the data overlay

filename

name of the file that should be used when downloading the source

type

type of the data overlay (default: GENERIC). Available options: GENERIC, GENETIC_VARIANT

3.3. Response Fields
Path	Type	Description
name

String

name

description

String

description

idObject

Number

identifier

publicOverlay

Boolean

is the data overlay publicly available to all users

order

Number

sort order

type

String

type; available options: GENERIC, GENETIC_VARIANT

genomeType

String

reference genome type; available options: UCSC

genomeVersion

String

reference genome version

creator

String

login of the user who uploaded data overlay

3.4. CURL sample from file
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/' -X POST \
    -d 'fileId=738&name=overlay+name&description=overlay+name&filename=overlay+name&type=GENERIC' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
3.5. Sample Response from file
{
  "name" : "overlay name",
  "creator" : "admin",
  "description" : "overlay name",
  "genomeType" : null,
  "genomeVersion" : null,
  "idObject" : 1000131,
  "publicOverlay" : false,
  "type" : "GENERIC",
  "order" : 1
}
3.6. CURL sample from content
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/' -X POST \
    -d 'content=element_identifier%09value%0A%09-1&name=overlay+name&description=overlay+description&filename=source.txt&type=GENERIC' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
3.7. Sample Response from content
{
  "name" : "overlay name",
  "creator" : "admin",
  "description" : "overlay description",
  "genomeType" : null,
  "genomeVersion" : null,
  "idObject" : 1000103,
  "publicOverlay" : false,
  "type" : "GENERIC",
  "order" : 1
}
4. Update overlay
4.1. Path Parameters
Table 4. /minerva/api/projects/{projectId}/overlays/{overlayId}
Parameter	Description
projectId

project identifier

overlayId

overlay identifier

4.2. Request Fields
Path	Type	Description
overlay.name

String

name

overlay.description

String

description

overlay.publicOverlay

Boolean

is the data overlay publicly available to all users

overlay.order

Number

sort order

overlay.type

String

type; available options: GENERIC, GENETIC_VARIANT

overlay.creator

String

login of the user who uploaded data overlay

4.3. Response Fields
Path	Type	Description
name

String

name

description

String

description

idObject

Number

identifier

publicOverlay

Boolean

is the data overlay publicly available to all users

order

Number

sort order

type

String

type; available options: GENERIC, GENETIC_VARIANT

genomeType

String

reference genome type; available options: UCSC

genomeVersion

String

reference genome version

creator

String

login of the user who uploaded data overlay

4.4. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/1000114' -X PATCH \
    -d '{"overlay":{"name":"test title","creator":"test_user","description":"test description","publicOverlay":false,"type":"GENERIC","order":0}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
4.5. Sample Response
{
  "name" : "test title",
  "creator" : "test_user",
  "description" : "test description",
  "genomeType" : null,
  "genomeVersion" : null,
  "idObject" : 1000114,
  "publicOverlay" : false,
  "type" : "GENERIC",
  "order" : 0
}
5. Delete overlay
5.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/1000160' -X DELETE \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
5.2. Path Parameters
Table 5. /minerva/api/projects/{projectId}/overlays/{overlayId}
Parameter	Description
projectId

project identifier

overlayId

overlay identifier

6. Download source data
6.1. Path Parameters
Table 6. /minerva/api/projects/{projectId}/overlays/{overlayId}:downloadSource
Parameter	Description
projectId

project identifier

overlayId

overlay identifier

6.2. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/1000140:downloadSource' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
6.3. Sample Response
element_identifier	value
	-1
7. Download legend
7.1. Path Parameters
Unresolved directive in project_overlays.adoc - include::../../../target/generated-snippets/projects/project_legend/download_source/path-parameters.adoc[]

7.2. CURL sample
Unresolved directive in project_overlays.adoc - include::../../../target/generated-snippets/projects/project_legend/download_source/curl-request.adoc[]

8. Get list of associated bioEntites
8.1. Path Parameters
Table 7. /minerva/api/projects/{projectId}/overlays/{overlayId}/models/{mapId}/bioEntities/
Parameter	Description
projectId

project identifier

mapId

map identifier

overlayId

overlay identifier

8.2. Response Fields
Path	Type	Description
[].type

String

type of bioEntity (ALIAS/REACTION)

[].overlayContent.idObject

String

identifier of the bioEntity

[].overlayContent.modelId

Number

map identifier where bioEntity is located

[].overlayContent.value

Number

normalized value assigned to the bioEntity from overlay

[].overlayContent.color

Object

color assigned to the bioEntity from overlay

[].overlayContent.description

String

description assigned to the bioEntity from overlay

[].overlayContent.sourceData

String

source data

[].overlayContent.geneVariations

Array

list of gene variants assigned to the bioEntity from overlay

[].overlayContent.width

Number

line width of reaction bioEntity assigned to the bioEntity from overlay

8.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/1000146/models/*/bioEntities/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
8.4. Sample Response
[ {
  "type" : "ALIAS",
  "overlayContent" : {
    "modelId" : 1142,
    "idObject" : "2848",
    "value" : 1.0,
    "color" : null,
    "description" : null,
    "type" : "GENERIC",
    "uniqueId" : 2848,
    "sourceData" : null
  }
}, {
  "type" : "ALIAS",
  "overlayContent" : {
    "modelId" : 1142,
    "idObject" : "2852",
    "value" : 1.0,
    "color" : null,
    "description" : null,
    "type" : "GENERIC",
    "uniqueId" : 2852,
    "sourceData" : null
  }
}, {
  "type" : "ALIAS",
  "overlayContent" : {
    "modelId" : 1142,
    "idObject" : "2851",
    "value" : 1.0,
    "color" : null,
    "description" : null,
    "type" : "GENERIC",
    "uniqueId" : 2851,
    "sourceData" : null
  }
}, {
  "type" : "ALIAS",
  "overlayContent" : {
    "modelId" : 1142,
    "idObject" : "2849",
    "value" : 1.0,
    "color" : null,
    "description" : null,
    "type" : "GENERIC",
    "uniqueId" : 2849,
    "sourceData" : null
  }
}, {
  "type" : "REACTION",
  "overlayContent" : {
    "modelId" : 1142,
    "idObject" : "574",
    "value" : -1.0,
    "color" : null,
    "description" : null,
    "type" : "GENERIC",
    "uniqueId" : 574,
    "sourceData" : null,
    "width" : null
  }
}, {
  "type" : "ALIAS",
  "overlayContent" : {
    "modelId" : 1143,
    "idObject" : "2850",
    "value" : 1.0,
    "color" : null,
    "description" : null,
    "type" : "GENERIC",
    "uniqueId" : 2850,
    "sourceData" : null
  }
} ]
9. Get reaction data
9.1. Path Parameters
Table 8. /minerva/api/projects/{projectId}/overlays/{overlayId}/models/{mapId}/bioEntities/reactions/{reactionId}/
Parameter	Description
projectId

project identifier

mapId

map identifier

overlayId

overlay identifier

reactionId

reaction identifier

9.2. Response Fields
Path	Type	Description
[].type

String

type of bioEntity (ALIAS/REACTION)

[].overlayContent.idObject

String

identifier of the bioEntity

[].overlayContent.modelId

Number

map identifier where bioEntity is located

[].overlayContent.value

Number

normalized value assigned to the bioEntity from overlay

[].overlayContent.color

Object

color assigned to the bioEntity from overlay

[].overlayContent.description

String

description assigned to the bioEntity from overlay

[].overlayContent.sourceData

String

source data

[].overlayContent.geneVariations

Array

list of gene variants assigned to the bioEntity from overlay

[].overlayContent.width

Number

line width of reaction bioEntity assigned to the bioEntity from overlay

9.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/1000100/models/1046/bioEntities/reactions/526/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
9.4. Sample Response
[ {
  "type" : "REACTION",
  "overlayContent" : {
    "modelId" : 1046,
    "idObject" : "526",
    "value" : -1.0,
    "color" : null,
    "description" : null,
    "type" : "GENERIC",
    "geneVariations" : [ ],
    "uniqueId" : 526,
    "sourceData" : null,
    "width" : null
  }
} ]
10. Get element data
10.1. Path Parameters
Table 9. /minerva/api/projects/{projectId}/overlays/{overlayId}/models/{mapId}/bioEntities/elements/{elementId}/
Parameter	Description
projectId

project identifier

mapId

map identifier

overlayId

overlay identifier

elementId

element identifier

10.2. Response Fields
Path	Type	Description
[].type

String

type of bioEntity (ALIAS/REACTION)

[].overlayContent.idObject

String

identifier of the bioEntity

[].overlayContent.modelId

Number

map identifier where bioEntity is located

[].overlayContent.value

Number

normalized value assigned to the bioEntity from overlay

[].overlayContent.color

Object

color assigned to the bioEntity from overlay

[].overlayContent.description

String

description assigned to the bioEntity from overlay

[].overlayContent.sourceData

String

source data

[].overlayContent.geneVariations

Array

list of gene variants assigned to the bioEntity from overlay

[].overlayContent.width

Number

line width of reaction bioEntity assigned to the bioEntity from overlay

10.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project/overlays/1000152/models/1154/bioEntities/elements/2881/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
10.4. Sample Response
[ {
  "type" : "ALIAS",
  "overlayContent" : {
    "modelId" : 1154,
    "idObject" : "2881",
    "value" : -1.0,
    "color" : null,
    "description" : null,
    "type" : "GENERIC",
    "geneVariations" : [ ],
    "uniqueId" : 2881,
    "sourceData" : null
  }
} ]

. Grant privilege
Grant access to the project.

1.1. Path Parameters
Table 1. /minerva/api/projects/{projectId}:grantPrivileges
Parameter	Description
projectId

project identifier

1.2. Request Fields
Path	Type	Description
[]

Array

list of privileges to grant

[].privilegeType

String

type of privilege (READ_PROJECT/WRITE_PROJECT)

[].login

String

user login who should gain access

1.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project:grantPrivileges' -X PATCH \
    -d '[{"privilegeType":"READ_PROJECT", "login":"curator_user"}]' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
2. Revoke privilege
Revoke access to the project.

2.1. Path Parameters
Table 2. /minerva/api/projects/{projectId}:revokePrivileges
Parameter	Description
projectId

project identifier

2.2. Request Fields
Path	Type	Description
[]

Array

list of privileges to revoke

[].privilegeType

String

type of privilege (READ_PROJECT/WRITE_PROJECT)

[].login

String

user login who should lose access

2.3. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/projects/test_project:revokePrivileges' -X PATCH \
    -d '[{"privilegeType":"READ_PROJECT", "login":"curator_user"}]' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'



Rest API Documentation - Taxonomy
minerva
version 18.2.1 2025-04-24T11:05:57Z
API-docs

Table of Contents
1. Get information about taxonomy
1.1. CURL sample
1.2. Path Parameters
1.3. Response Fields
1.4. Sample Response
1. Get information about taxonomy
1.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/taxonomy/9606/' -X GET
1.2. Path Parameters
Table 1. /minerva/api/taxonomy/{taxonomyId}/
Parameter	Description
taxonomyId

taxonomy id

1.3. Response Fields
Path	Type	Description
name

String

name

id

String

taxonomy id

1.4. Sample Response
{
  "name" : "Homo sapiens",
  "id" : "9606"
}




Rest API Documentation - Users
minerva
version 18.2.1 2025-04-24T11:05:57Z
API-docs

Table of Contents
1. List all users
1.1. CURL sample
1.2. Response Fields
1.3. Sample Response
2. Get specific user data
2.1. CURL sample
2.2. Path Parameters
2.3. Response Fields
2.4. Sample Response
3. Create user
3.1. CURL sample
3.2. Path Parameters
3.3. Request Parameters
3.4. Response Fields
3.5. Sample Response
4. Update user
4.1. CURL sample
4.2. Path Parameters
4.3. Request Parameters
4.4. Response Fields
4.5. Sample Response
5. Update user privileges
5.1. Path Parameters
5.2. Request Fields
5.3. Response Fields
5.4. CURL sample 1
5.5. Sample Response 1
5.6. CURL sample 2
5.7. Sample Response 2
6. Update user preferences
6.1. Path Parameters
6.2. Request Fields
6.3. Response Fields
6.4. CURL sample 1
6.5. CURL sample 2
6.6. CURL sample 3
6.7. CURL sample 4
6.8. CURL sample 5
6.9. Sample Response 5
7. Delete user
7.1. CURL sample
7.2. Path Parameters
8. Request password reset over email
8.1. CURL sample
8.2. Path Parameters
9. Reset password using token obtained over email
9.1. CURL sample
9.2. Request Parameters
10. Register new user
10.1. CURL sample
10.2. Request Fields
10.3. Response Fields
10.4. Sample Response
11. Confirm email
11.1. CURL sample
11.2. Request Parameters
11.3. Path Parameters
11.4. Response Fields
11.5. Sample Response
1. List all users
1.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
1.2. Response Fields
Path	Type	Description
[]

Array

list of users

[].login

String

user login

[].connectedToLdap

Boolean

is user account connected to LDAP

[].ldapAccountAvailable

Boolean

does the account exist in LDAP

[].active

Boolean

ist the use account active (can user login)

[].confirmed

Boolean

is the user email confirmed

[].email

String

email address

[].orcidId

String

orcid identifier

[].id

Number

user unique id

[].maxColor

color

color used for drawing data overlays with max value

[].minColor

color

color used for drawing data overlays with min value

[].neutralColor

color

color used for drawing data overlays with 0 value

[].simpleColor

color

color used for drawing data overlays without value

[].name

String

first name

[].surname

String

last name

[].removed

Boolean

is the account removed

[].termsOfUseConsent

Boolean

did user agree to terms of use

[].privileges

Array

list of user privileges

[].privileges[].objectId

String

object id to which project has privilege

[].lastActive

String

datetime of the last activity in the active session

[].privileges[].privilegeType

String

type of privilege, available values: IS_ADMIN, IS_CURATOR, READ_PROJECT, WRITE_PROJECT

1.3. Sample Response
[ {
  "id" : 782,
  "login" : "test_user",
  "name" : null,
  "surname" : null,
  "email" : null,
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ ],
  "active" : true,
  "confirmed" : true,
  "ldapAccountAvailable" : false,
  "lastActive" : "2025-04-24 11:19:01"
}, {
  "id" : 3,
  "login" : "anonymous",
  "name" : "",
  "surname" : "",
  "email" : null,
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ {
    "privilegeType" : "READ_PROJECT",
    "objectId" : "empty"
  } ],
  "active" : true,
  "confirmed" : true,
  "ldapAccountAvailable" : false,
  "lastActive" : null
}, {
  "id" : 1,
  "login" : "admin",
  "name" : "",
  "surname" : "",
  "email" : "",
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ {
    "privilegeType" : "IS_CURATOR",
    "objectId" : null
  }, {
    "privilegeType" : "WRITE_PROJECT",
    "objectId" : "empty"
  }, {
    "privilegeType" : "READ_PROJECT",
    "objectId" : "empty"
  }, {
    "privilegeType" : "IS_ADMIN",
    "objectId" : null
  } ],
  "active" : true,
  "confirmed" : true,
  "ldapAccountAvailable" : false,
  "lastActive" : "2025-04-24 11:25:10"
} ]
2. Get specific user data
2.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user' -X GET \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx"
2.2. Path Parameters
Table 1. /minerva/api/users/{login}
Parameter	Description
login

user login

2.3. Response Fields
Path	Type	Description
login

String

user login

connectedToLdap

Boolean

is user account connected to LDAP

ldapAccountAvailable

Boolean

does the account exist in LDAP

active

Boolean

ist the use account active (can user login)

confirmed

Boolean

is the user email confirmed

email

String

email address

orcidId

String

orcid identifier

id

Number

user unique id

maxColor

color

color used for drawing data overlays with max value

minColor

color

color used for drawing data overlays with min value

neutralColor

color

color used for drawing data overlays with 0 value

simpleColor

color

color used for drawing data overlays without value

name

String

first name

surname

String

last name

removed

Boolean

is the account removed

termsOfUseConsent

Boolean

did user agree to terms of use

privileges

Array

list of user privileges

privileges[].objectId

String

object id to which project has privilege

lastActive

String

datetime of the last activity in the active session

privileges[].privilegeType

String

type of privilege, available values: IS_ADMIN, IS_CURATOR, READ_PROJECT, WRITE_PROJECT

2.4. Sample Response
{
  "id" : 812,
  "login" : "test_user",
  "name" : null,
  "surname" : null,
  "email" : null,
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ ],
  "active" : true,
  "confirmed" : true,
  "ldapAccountAvailable" : false,
  "lastActive" : "2025-04-24 11:25:18"
}
3. Create user
3.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_login' -X POST \
    -d 'name=Name&password=Password' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/x-www-form-urlencoded'
3.2. Path Parameters
Table 2. /minerva/api/users/{login}
Parameter	Description
login

user login

3.3. Request Parameters
Parameter	Description
name

first name

surname

last name

password

user password

email

email address

defaultPrivileges

should the default privileges be added to the user after user creation

3.4. Response Fields
Path	Type	Description
login

String

user login

connectedToLdap

Boolean

is user account connected to LDAP

ldapAccountAvailable

Boolean

does the account exist in LDAP

active

Boolean

ist the use account active (can user login)

confirmed

Boolean

is the user email confirmed

email

String

email address

orcidId

String

orcid identifier

id

Number

user unique id

maxColor

color

color used for drawing data overlays with max value

minColor

color

color used for drawing data overlays with min value

neutralColor

color

color used for drawing data overlays with 0 value

simpleColor

color

color used for drawing data overlays without value

name

String

first name

surname

String

last name

removed

Boolean

is the account removed

termsOfUseConsent

Boolean

did user agree to terms of use

privileges

Array

list of user privileges

privileges[].objectId

String

object id to which project has privilege

lastActive

String

datetime of the last activity in the active session

privileges[].privilegeType

String

type of privilege, available values: IS_ADMIN, IS_CURATOR, READ_PROJECT, WRITE_PROJECT

3.5. Sample Response
{
  "id" : 786,
  "login" : "test_login",
  "name" : "Name",
  "surname" : null,
  "email" : null,
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ ],
  "active" : true,
  "confirmed" : true,
  "ldapAccountAvailable" : false,
  "lastActive" : null
}
4. Update user
4.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user' -X PATCH \
    -d '{"user":{"password":"new pass"}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
4.2. Path Parameters
Table 3. /minerva/api/users/{login}
Parameter	Description
login

user login

4.3. Request Parameters
Parameter	Description
password

user password

connectedToLdap

is user account connected to LDAP

ldapAccountAvailable

does is account exist in LDAP

email

email address

maxColor

color used for drawing data overlays with max value

minColor

color used for drawing data overlays with min value

neutralColor

color used for drawing data overlays with 0 value

simpleColor

color used for drawing data overlays without value

name

first name

surname

last name

4.4. Response Fields
Path	Type	Description
login

String

user login

connectedToLdap

Boolean

is user account connected to LDAP

ldapAccountAvailable

Boolean

does the account exist in LDAP

active

Boolean

ist the use account active (can user login)

confirmed

Boolean

is the user email confirmed

email

String

email address

orcidId

String

orcid identifier

id

Number

user unique id

maxColor

color

color used for drawing data overlays with max value

minColor

color

color used for drawing data overlays with min value

neutralColor

color

color used for drawing data overlays with 0 value

simpleColor

color

color used for drawing data overlays without value

name

String

first name

surname

String

last name

removed

Boolean

is the account removed

termsOfUseConsent

Boolean

did user agree to terms of use

privileges

Array

list of user privileges

privileges[].objectId

String

object id to which project has privilege

lastActive

String

datetime of the last activity in the active session

privileges[].privilegeType

String

type of privilege, available values: IS_ADMIN, IS_CURATOR, READ_PROJECT, WRITE_PROJECT

4.5. Sample Response
{
  "id" : 817,
  "login" : "test_user",
  "name" : null,
  "surname" : null,
  "email" : null,
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ ],
  "active" : true,
  "confirmed" : true,
  "ldapAccountAvailable" : false,
  "lastActive" : "2025-04-24 11:25:20"
}
5. Update user privileges
5.1. Path Parameters
Table 4. /minerva/api/users/{login}:updatePrivileges
Parameter	Description
login

user login

5.2. Request Fields
Path	Type	Description
privileges.*

Boolean

should the privilege defined as PRIVILEGE_TYPE:ID_OBJECT be granted or not

5.3. Response Fields
Path	Type	Description
login

String

user login

connectedToLdap

Boolean

is user account connected to LDAP

ldapAccountAvailable

Boolean

does the account exist in LDAP

active

Boolean

ist the use account active (can user login)

confirmed

Boolean

is the user email confirmed

email

String

email address

orcidId

String

orcid identifier

id

Number

user unique id

maxColor

color

color used for drawing data overlays with max value

minColor

color

color used for drawing data overlays with min value

neutralColor

color

color used for drawing data overlays with 0 value

simpleColor

color

color used for drawing data overlays without value

name

String

first name

surname

String

last name

removed

Boolean

is the account removed

termsOfUseConsent

Boolean

did user agree to terms of use

privileges

Array

list of user privileges

privileges[].objectId

String

object id to which project has privilege

lastActive

String

datetime of the last activity in the active session

privileges[].privilegeType

String

type of privilege, available values: IS_ADMIN, IS_CURATOR, READ_PROJECT, WRITE_PROJECT

5.4. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:updatePrivileges' -X PATCH \
    -d '{"privileges":{"IS_ADMIN":true}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
5.5. Sample Response 1
{
  "id" : 794,
  "login" : "test_user",
  "name" : null,
  "surname" : null,
  "email" : null,
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ {
    "privilegeType" : "IS_ADMIN",
    "objectId" : null
  } ],
  "active" : true,
  "confirmed" : true,
  "ldapAccountAvailable" : false,
  "lastActive" : "2025-04-24 11:25:12"
}
5.6. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:updatePrivileges' -X PATCH \
    -d '{"privileges":{"READ_PROJECT:test_project":true}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
5.7. Sample Response 2
{
  "id" : 793,
  "login" : "test_user",
  "name" : null,
  "surname" : null,
  "email" : null,
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ {
    "privilegeType" : "READ_PROJECT",
    "objectId" : "test_project"
  } ],
  "active" : true,
  "confirmed" : true,
  "ldapAccountAvailable" : false,
  "lastActive" : "2025-04-24 11:25:12"
}
6. Update user preferences
6.1. Path Parameters
Table 5. /minerva/api/users/{login}:updatePreferences
Parameter	Description
login

user login

6.2. Request Fields
Path	Type	Description
preferences

Object

information about default preferences

preferences.project-upload

Object

definition of preferences for project-upload.

preferences.project-upload.annotate-model

Boolean

annotate model after it is uploaded.

preferences.project-upload.auto-resize

Boolean

auto resize map after parsing

preferences.project-upload.cache-data

Boolean

cache all the data for project

preferences.project-upload.sbgn

Boolean

visualize project in sbgn-like view

preferences.project-upload.semantic-zooming-contains-multiple-overlays

Boolean

display each semantic zoom level in separate overlay.

preferences.project-upload.validate-miriam

Boolean

validate all miriam annotations

preferences.element-annotators

Object

definition of element annotators used by user

preferences.element-annotators['*']

Array

list of annotators used for specific BioEntity type. Type of BioEntity is a class name that represents specific type in the system, for example: lcsb.mapviewer.model.map.BioEntity, lcsb.mapviewer.model.map.species.Complex

preferences.element-annotators['*'][].id

String

id

preferences.element-annotators['*'][].annotatorClass

String

type of annotator

preferences.element-annotators['*'][].order

Number

defines order in which annotators should be used

preferences.element-annotators['*'][].parameters

Array

list of parameters for the annotator

preferences.element-annotators['*'][].parameters[].type

String

is this parameter INPUT/OUTPUT/CONFIG type. INPUT types define what should be used to identify the element. OUTPUT parameter defines what should be written to the element.

preferences.element-annotators['*'][].parameters[].annotation_type

String

specifies annotation type to be used (if empty then field will be used)

preferences.element-annotators['*'][].parameters[].field

String

specifies field to be used

preferences.element-annotators['*'][].parameters[].name

String

name of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].commonName

String

readable name of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].inputType

String

class type of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].description

String

description of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].value

String

value of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].order

Number

input parameters are checked in order. First match identifies the element. This field defines what is the order of INPUT parameters.

preferences.element-required-annotations

Object

definition of required annotation by BioEntity type.

preferences.element-required-annotations['*']

Object

definition of required annotations for specific BioEntity type

preferences.element-required-annotations['*'].require-at-least-one

Boolean

is at least one annotation required

preferences.element-required-annotations['*'].annotation-list

Array

list of annotation types from which at least one is required

preferences.element-valid-annotations

Object

definition of valid annotation by BioEntity type.

preferences.element-valid-annotations['*'][]

Array

list of annotation types that is valid for specific BioEntity type

preferences.gui-preferences

Object

definition of user gui preferences.

preferences.gui-preferences.*

String

key-value definition of gui preference used for remembering default sort order, default pagination, etc

6.3. Response Fields
Path	Type	Description
preferences

Object

set of user preferences

preferences.element-annotators

Object

definition of element annotators used by user

preferences.element-annotators['*']

Array

list of annotators used for specific BioEntity type. Type of BioEntity is a class name that represents specific type in the system, for example: lcsb.mapviewer.model.map.BioEntity, lcsb.mapviewer.model.map.species.Complex

preferences.element-annotators['*'][].annotatorClass

String

type of annotator

preferences.element-annotators['*'][].order

Number

defines order in which annotators should be used

preferences.element-annotators['*'][].parameters

Array

list of parameters for the annotator

preferences.element-annotators['*'][].parameters[].type

String

is this parameter INPUT/OUTPUT/CONFIG type. INPUT types define what should be used to identify the element. OUTPUT parameter defines what should be written to the element.

preferences.element-annotators['*'][].parameters[].annotation_type

String

specifies annotation type to be used (if empty then field will be used)

preferences.element-annotators['*'][].parameters[].field

String

specifies field to be used

preferences.element-annotators['*'][].parameters[].name

String

name of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].commonName

String

readable name of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].inputType

String

class type of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].description

String

description of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].value

String

value of the CONFIG parameter type

preferences.element-annotators['*'][].parameters[].order

Number

input parameters are checked in order. First match identifies the element. This field defines what is the order of INPUT parameters.

preferences.element-required-annotations

Object

definition of required annotation by BioEntity type.

preferences.element-required-annotations['*']

Object

definition of required annotations for specific BioEntity type

preferences.element-required-annotations['*'].require-at-least-one

Boolean

is at least one annotation required

preferences.element-required-annotations['*'].annotation-list

Array

list of annotation types from which at least one is required

preferences.element-valid-annotations

Object

definition of valid annotation by BioEntity type.

preferences.element-valid-annotations['*'][]

Array

list of annotation types that is valid for specific BioEntity type

preferences.gui-preferences

Object

definition of user gui preferences.

preferences.gui-preferences.*

String

key-value definition of gui preference used for remembering default sort order, default pagination, etc

preferences.project-upload

Object

definition of preferences for project-upload.

preferences.project-upload.annotate-model

Boolean

annotate model after it is uploaded.

preferences.project-upload.auto-resize

Boolean

auto resize map after parsing

preferences.project-upload.cache-data

Boolean

cache all the data for project

preferences.project-upload.sbgn

Boolean

visualize project in sbgn-like view

preferences.project-upload.semantic-zooming-contains-multiple-overlays

Boolean

display each semantic zoom level in separate overlay.

preferences.project-upload.validate-miriam

Boolean

validate all miriam annotations

6.4. CURL sample 1
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:updatePreferences' -X PATCH \
    -d '{"preferences":{"project-upload":{"validate-miriam":true,"annotate-model":true,"cache-data":true,"auto-resize":true,"semantic-zooming-contains-multiple-overlays":true,"sbgn":true},"element-annotators":{},"element-required-annotations":{},"element-valid-annotations":{},"gui-preferences":{}}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
6.5. CURL sample 2
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:updatePreferences' -X PATCH \
    -d '{"preferences":{"project-upload":{"validate-miriam":false,"annotate-model":false,"cache-data":true,"auto-resize":true,"semantic-zooming-contains-multiple-overlays":false,"sbgn":false},"element-annotators":{"lcsb.mapviewer.model.map.species.Gene":[{"id":null,"order":0,"annotatorClass":"lcsb.mapviewer.annotation.services.annotators.UniprotAnnotator","parameters":[{"field":null,"annotation_type":"UNIPROT","order":0,"type":"INPUT"},{"field":"NAME","annotation_type":"UNIPROT","order":1,"type":"INPUT"},{"field":null,"annotation_type":"HGNC_SYMBOL","order":2,"type":"OUTPUT"},{"field":null,"annotation_type":"UNIPROT","order":3,"type":"OUTPUT"},{"field":null,"annotation_type":"EC","order":4,"type":"OUTPUT"},{"field":null,"annotation_type":"ENTREZ","order":5,"type":"OUTPUT"},{"type":"KEGG_ORGANISM_IDENTIFIER","name":"KEGG_ORGANISM_IDENTIFIER","commonName":"KEGG organism identifier","inputType":"java.lang.String","description":"Space-delimited list of organisms codes for which homologous genes (final GENE section in the KEGG enzyme record) should be imported. Currently only ATH (final Arabidopsis Thaliana) is supported.","value":"XXX","order":6,"type":"CONFIG"}]}]},"element-required-annotations":{},"element-valid-annotations":{},"gui-preferences":{}}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
6.6. CURL sample 3
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:updatePreferences' -X PATCH \
    -d '{"preferences":{"project-upload":{"validate-miriam":false,"annotate-model":false,"cache-data":true,"auto-resize":true,"semantic-zooming-contains-multiple-overlays":false,"sbgn":false},"element-annotators":{},"element-required-annotations":{"lcsb.mapviewer.model.map.species.Protein":{"require-at-least-one":true,"annotation-list":["HGNC","HGNC_SYMBOL"]},"lcsb.mapviewer.model.map.species.SimpleMolecule":{"require-at-least-one":false,"annotation-list":["CHEBI"]}},"element-valid-annotations":{},"gui-preferences":{}}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
6.7. CURL sample 4
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:updatePreferences' -X PATCH \
    -d '{"preferences":{"project-upload":{"validate-miriam":false,"annotate-model":false,"cache-data":true,"auto-resize":true,"semantic-zooming-contains-multiple-overlays":false,"sbgn":false},"element-annotators":{},"element-required-annotations":{},"element-valid-annotations":{"lcsb.mapviewer.model.map.species.Gene":["HGNC"]},"gui-preferences":{}}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
6.8. CURL sample 5
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:updatePreferences' -X PATCH \
    -d '{"preferences":{"project-upload":{"validate-miriam":false,"annotate-model":false,"cache-data":true,"auto-resize":true,"semantic-zooming-contains-multiple-overlays":false,"sbgn":false},"element-annotators":{},"element-required-annotations":{},"element-valid-annotations":{},"gui-preferences":{"admin-projects-datatable-order":"1-asc"}}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
6.9. Sample Response 5
{
  "preferences" : {
    "project-upload" : {
      "validate-miriam" : false,
      "annotate-model" : false,
      "cache-data" : true,
      "auto-resize" : true,
      "semantic-zooming-contains-multiple-overlays" : false,
      "sbgn" : false
    },
    "element-annotators" : {
      "lcsb.mapviewer.model.map.species.AntisenseRna" : [ ],
      "lcsb.mapviewer.model.map.compartment.BottomSquareCompartment" : [ {
        "id" : 442,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.Complex" : [ {
        "id" : 443,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.Degraded" : [ ],
      "lcsb.mapviewer.model.map.species.Drug" : [ ],
      "lcsb.mapviewer.model.map.species.Gene" : [ {
        "id" : 444,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.HgncAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 2,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENSEMBL",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENTREZ",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "REFSEQ",
          "order" : 7,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "UNIPROT",
          "order" : 8,
          "type" : "OUTPUT"
        }, {
          "field" : "SYMBOL",
          "annotation_type" : null,
          "order" : 9,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 10,
          "type" : "OUTPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 11,
          "type" : "OUTPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 12,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.GenericProtein" : [ {
        "id" : 445,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.HgncAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 2,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENSEMBL",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENTREZ",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "REFSEQ",
          "order" : 7,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "UNIPROT",
          "order" : 8,
          "type" : "OUTPUT"
        }, {
          "field" : "SYMBOL",
          "annotation_type" : null,
          "order" : 9,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 10,
          "type" : "OUTPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 11,
          "type" : "OUTPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 12,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.Ion" : [ {
        "id" : 446,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.ChebiAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "CHEBI",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "INCHI",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "INCHIKEY",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "STITCH",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : "SMILE",
          "annotation_type" : null,
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 7,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.IonChannelProtein" : [ {
        "id" : 447,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.HgncAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 2,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENSEMBL",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENTREZ",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "REFSEQ",
          "order" : 7,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "UNIPROT",
          "order" : 8,
          "type" : "OUTPUT"
        }, {
          "field" : "SYMBOL",
          "annotation_type" : null,
          "order" : 9,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 10,
          "type" : "OUTPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 11,
          "type" : "OUTPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 12,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.compartment.LeftSquareCompartment" : [ {
        "id" : 448,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.compartment.OvalCompartment" : [ {
        "id" : 449,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.compartment.PathwayCompartment" : [ {
        "id" : 450,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.Phenotype" : [ {
        "id" : 451,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.ReceptorProtein" : [ {
        "id" : 452,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.HgncAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 2,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENSEMBL",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENTREZ",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "REFSEQ",
          "order" : 7,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "UNIPROT",
          "order" : 8,
          "type" : "OUTPUT"
        }, {
          "field" : "SYMBOL",
          "annotation_type" : null,
          "order" : 9,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 10,
          "type" : "OUTPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 11,
          "type" : "OUTPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 12,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.compartment.RightSquareCompartment" : [ {
        "id" : 453,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.Rna" : [ {
        "id" : 454,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.HgncAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 2,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENSEMBL",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENTREZ",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "REFSEQ",
          "order" : 7,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "UNIPROT",
          "order" : 8,
          "type" : "OUTPUT"
        }, {
          "field" : "SYMBOL",
          "annotation_type" : null,
          "order" : 9,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 10,
          "type" : "OUTPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 11,
          "type" : "OUTPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 12,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.SimpleMolecule" : [ {
        "id" : 455,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.ChebiAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "CHEBI",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "INCHI",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "INCHIKEY",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "STITCH",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : "SMILE",
          "annotation_type" : null,
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 7,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.compartment.SquareCompartment" : [ {
        "id" : 456,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.compartment.TopSquareCompartment" : [ {
        "id" : 457,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.TruncatedProtein" : [ {
        "id" : 458,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.HgncAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 2,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENSEMBL",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENTREZ",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "REFSEQ",
          "order" : 7,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "UNIPROT",
          "order" : 8,
          "type" : "OUTPUT"
        }, {
          "field" : "SYMBOL",
          "annotation_type" : null,
          "order" : 9,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 10,
          "type" : "OUTPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 11,
          "type" : "OUTPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 12,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.Unknown" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.CatalysisReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.DissociationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.HeterodimerAssociationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.InhibitionReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.KnownTransitionOmittedReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.ModulationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.NegativeInfluenceReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.PhysicalStimulationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.PositiveInfluenceReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.ReducedModulationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.ReducedPhysicalStimulationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.ReducedTriggerReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.StateTransitionReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.TranscriptionReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.TranslationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.TransportReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.TriggerReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.TruncationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownCatalysisReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownInhibitionReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownNegativeInfluenceReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownPositiveInfluenceReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedModulationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedPhysicalStimulationReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedTriggerReaction" : [ ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownTransitionReaction" : [ ],
      "lcsb.mapviewer.model.map.BioEntity" : [ ],
      "lcsb.mapviewer.model.map.species.Element" : [ ],
      "lcsb.mapviewer.model.map.reaction.Reaction" : [ ],
      "lcsb.mapviewer.model.map.compartment.Compartment" : [ {
        "id" : 459,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.GoAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "GO",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "OUTPUT"
        }, {
          "field" : "DESCRIPTION",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.Species" : [ ],
      "lcsb.mapviewer.model.map.species.Chemical" : [ {
        "id" : 460,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.ChebiAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "CHEBI",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 2,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "INCHI",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "INCHIKEY",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "STITCH",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : "SMILE",
          "annotation_type" : null,
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 7,
          "type" : "OUTPUT"
        } ]
      } ],
      "lcsb.mapviewer.model.map.species.Protein" : [ {
        "id" : 461,
        "order" : 0,
        "annotatorClass" : "lcsb.mapviewer.annotation.services.annotators.HgncAnnotator",
        "parameters" : [ {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 0,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 1,
          "type" : "INPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 2,
          "type" : "INPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENSEMBL",
          "order" : 3,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "ENTREZ",
          "order" : 4,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC",
          "order" : 5,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "HGNC_SYMBOL",
          "order" : 6,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "REFSEQ",
          "order" : 7,
          "type" : "OUTPUT"
        }, {
          "field" : null,
          "annotation_type" : "UNIPROT",
          "order" : 8,
          "type" : "OUTPUT"
        }, {
          "field" : "SYMBOL",
          "annotation_type" : null,
          "order" : 9,
          "type" : "OUTPUT"
        }, {
          "field" : "SYNONYMS",
          "annotation_type" : null,
          "order" : 10,
          "type" : "OUTPUT"
        }, {
          "field" : "NAME",
          "annotation_type" : null,
          "order" : 11,
          "type" : "OUTPUT"
        }, {
          "field" : "FULL_NAME",
          "annotation_type" : null,
          "order" : 12,
          "type" : "OUTPUT"
        } ]
      } ]
    },
    "element-required-annotations" : {
      "lcsb.mapviewer.model.map.BioEntity" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.Element" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.reaction.Reaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.compartment.Compartment" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.Species" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.reaction.type.CatalysisReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.DissociationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.HeterodimerAssociationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.InhibitionReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.KnownTransitionOmittedReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.ModulationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.NegativeInfluenceReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.PhysicalStimulationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.PositiveInfluenceReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.ReducedModulationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.ReducedPhysicalStimulationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.ReducedTriggerReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.StateTransitionReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.TranscriptionReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.TranslationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.TransportReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.TriggerReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.TruncationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.UnknownCatalysisReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.UnknownInhibitionReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.UnknownNegativeInfluenceReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.UnknownPositiveInfluenceReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedModulationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedPhysicalStimulationReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedTriggerReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.reaction.type.UnknownTransitionReaction" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBMED" ]
      },
      "lcsb.mapviewer.model.map.compartment.LeftSquareCompartment" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.compartment.BottomSquareCompartment" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.compartment.RightSquareCompartment" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.compartment.TopSquareCompartment" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.compartment.SquareCompartment" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.compartment.OvalCompartment" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.compartment.PathwayCompartment" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.AntisenseRna" : {
        "require-at-least-one" : true,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.Chemical" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBCHEM_SUBSTANCE", "PUBCHEM", "CHEBI", "CHEM_ID_PLUS" ]
      },
      "lcsb.mapviewer.model.map.species.Complex" : {
        "require-at-least-one" : true,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.Degraded" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.Drug" : {
        "require-at-least-one" : true,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.Gene" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "HGNC_SYMBOL", "HGNC" ]
      },
      "lcsb.mapviewer.model.map.species.Phenotype" : {
        "require-at-least-one" : true,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.Protein" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "HGNC_SYMBOL", "HGNC" ]
      },
      "lcsb.mapviewer.model.map.species.Rna" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "HGNC_SYMBOL", "HGNC" ]
      },
      "lcsb.mapviewer.model.map.species.Unknown" : {
        "require-at-least-one" : false,
        "annotation-list" : [ ]
      },
      "lcsb.mapviewer.model.map.species.Ion" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBCHEM_SUBSTANCE", "PUBCHEM", "CHEBI", "CHEM_ID_PLUS" ]
      },
      "lcsb.mapviewer.model.map.species.SimpleMolecule" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "PUBCHEM_SUBSTANCE", "PUBCHEM", "CHEBI", "CHEM_ID_PLUS" ]
      },
      "lcsb.mapviewer.model.map.species.TruncatedProtein" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "HGNC_SYMBOL", "HGNC" ]
      },
      "lcsb.mapviewer.model.map.species.GenericProtein" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "HGNC_SYMBOL", "HGNC" ]
      },
      "lcsb.mapviewer.model.map.species.IonChannelProtein" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "HGNC_SYMBOL", "HGNC" ]
      },
      "lcsb.mapviewer.model.map.species.ReceptorProtein" : {
        "require-at-least-one" : true,
        "annotation-list" : [ "HGNC_SYMBOL", "HGNC" ]
      }
    },
    "element-valid-annotations" : {
      "lcsb.mapviewer.model.map.BioEntity" : [ "PUBMED" ],
      "lcsb.mapviewer.model.map.species.Element" : [ "PUBMED" ],
      "lcsb.mapviewer.model.map.reaction.Reaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.compartment.Compartment" : [ "PUBMED", "GO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.species.Species" : [ "PUBMED" ],
      "lcsb.mapviewer.model.map.reaction.type.CatalysisReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.DissociationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.HeterodimerAssociationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.InhibitionReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.KnownTransitionOmittedReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.ModulationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.NegativeInfluenceReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.PhysicalStimulationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.PositiveInfluenceReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.ReducedModulationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.ReducedPhysicalStimulationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.ReducedTriggerReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.StateTransitionReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.TranscriptionReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.TranslationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.TransportReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.TriggerReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.TruncationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownCatalysisReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownInhibitionReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownNegativeInfluenceReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownPositiveInfluenceReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedModulationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedPhysicalStimulationReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownReducedTriggerReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.reaction.type.UnknownTransitionReaction" : [ "VMH_REACTION", "RGD", "COG", "DOI", "PUBMED", "REACTOME", "KEGG_PATHWAY", "RHEA", "KEGG_REACTION" ],
      "lcsb.mapviewer.model.map.compartment.LeftSquareCompartment" : [ "PUBMED", "GO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.compartment.BottomSquareCompartment" : [ "PUBMED", "GO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.compartment.RightSquareCompartment" : [ "PUBMED", "GO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.compartment.TopSquareCompartment" : [ "PUBMED", "GO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.compartment.SquareCompartment" : [ "PUBMED", "GO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.compartment.OvalCompartment" : [ "PUBMED", "GO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.compartment.PathwayCompartment" : [ "PUBMED", "GO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.species.AntisenseRna" : [ "PUBMED" ],
      "lcsb.mapviewer.model.map.species.Chemical" : [ "PUBCHEM_SUBSTANCE", "KEGG_COMPOUND", "HMDB", "PUBCHEM", "PUBMED", "CHEBI", "CHEM_ID_PLUS", "VMH_METABOLITE" ],
      "lcsb.mapviewer.model.map.species.Complex" : [ "CHEMBL_TARGET", "EC", "PUBMED", "GO", "INTERPRO", "MESH_2012" ],
      "lcsb.mapviewer.model.map.species.Degraded" : [ "PUBMED" ],
      "lcsb.mapviewer.model.map.species.Drug" : [ "CHEMBL_COMPOUND", "HMDB", "DRUGBANK", "PUBMED", "CHEBI", "CHEM_ID_PLUS" ],
      "lcsb.mapviewer.model.map.species.Gene" : [ "HGNC_SYMBOL", "PANTHER", "MGD", "REFSEQ", "PDB", "PUBMED", "ENTREZ", "ECO", "ENSEMBL", "UNIPROT", "HGNC", "KEGG_GENES" ],
      "lcsb.mapviewer.model.map.species.Phenotype" : [ "PUBMED", "GO", "MESH_2012", "OMIM" ],
      "lcsb.mapviewer.model.map.species.Protein" : [ "CHEMBL_TARGET", "PDB", "UNIPROT_ISOFORM", "EC", "ENTREZ", "ECO", "UNIPROT", "INTERPRO", "KEGG_GENES", "HGNC_SYMBOL", "PANTHER", "MGD", "REFSEQ", "PUBMED", "ENSEMBL", "HGNC" ],
      "lcsb.mapviewer.model.map.species.Rna" : [ "HGNC_SYMBOL", "PANTHER", "MGD", "REFSEQ", "PDB", "PUBMED", "ENTREZ", "ECO", "ENSEMBL", "UNIPROT", "HGNC", "KEGG_GENES" ],
      "lcsb.mapviewer.model.map.species.Unknown" : [ "PUBMED" ],
      "lcsb.mapviewer.model.map.species.Ion" : [ "PUBCHEM_SUBSTANCE", "KEGG_COMPOUND", "HMDB", "PUBCHEM", "PUBMED", "CHEBI", "CHEM_ID_PLUS", "VMH_METABOLITE" ],
      "lcsb.mapviewer.model.map.species.SimpleMolecule" : [ "PUBCHEM_SUBSTANCE", "KEGG_COMPOUND", "HMDB", "PUBCHEM", "PUBMED", "CHEBI", "CHEM_ID_PLUS", "VMH_METABOLITE" ],
      "lcsb.mapviewer.model.map.species.TruncatedProtein" : [ "CHEMBL_TARGET", "PDB", "UNIPROT_ISOFORM", "EC", "ENTREZ", "ECO", "UNIPROT", "INTERPRO", "KEGG_GENES", "HGNC_SYMBOL", "PANTHER", "MGD", "REFSEQ", "PUBMED", "ENSEMBL", "HGNC" ],
      "lcsb.mapviewer.model.map.species.GenericProtein" : [ "CHEMBL_TARGET", "PDB", "UNIPROT_ISOFORM", "EC", "ENTREZ", "ECO", "UNIPROT", "INTERPRO", "KEGG_GENES", "HGNC_SYMBOL", "PANTHER", "MGD", "REFSEQ", "PUBMED", "ENSEMBL", "HGNC" ],
      "lcsb.mapviewer.model.map.species.IonChannelProtein" : [ "CHEMBL_TARGET", "PDB", "UNIPROT_ISOFORM", "EC", "ENTREZ", "ECO", "UNIPROT", "INTERPRO", "KEGG_GENES", "HGNC_SYMBOL", "PANTHER", "MGD", "REFSEQ", "PUBMED", "ENSEMBL", "HGNC" ],
      "lcsb.mapviewer.model.map.species.ReceptorProtein" : [ "CHEMBL_TARGET", "PDB", "UNIPROT_ISOFORM", "EC", "ENTREZ", "ECO", "UNIPROT", "INTERPRO", "KEGG_GENES", "HGNC_SYMBOL", "PANTHER", "MGD", "REFSEQ", "PUBMED", "ENSEMBL", "HGNC" ]
    },
    "gui-preferences" : {
      "admin-projects-datatable-order" : "1-asc"
    }
  }
}
7. Delete user
7.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user' -X PATCH \
    -d '{"user":{"password":"new pass"}}' \
    --cookie "MINERVA_AUTH_TOKEN=xxxxxxxx" \
    -H 'Content-Type: application/json'
7.2. Path Parameters
Table 6. /minerva/api/users/{login}
Parameter	Description
login

user login

8. Request password reset over email
8.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:requestResetPassword' -X POST
8.2. Path Parameters
Table 7. /minerva/api/users/{login}:requestResetPassword
Parameter	Description
login

user login

9. Reset password using token obtained over email
9.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users:resetPassword' -X POST \
    -d 'token=06200200-0089-4048-8361-040080885770&password=pass2' \
    -H 'Content-Type: application/x-www-form-urlencoded'
9.2. Request Parameters
Parameter	Description
password

new password

token

reset password token obtained using email

10. Register new user
10.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users:registerUser' -X POST \
    -d '{"password":"123qweasdzxc","surname":"Gawron","name":"Piotr","email":"piotr.gawron@uni.lu"}' \
    -H 'Content-Type: application/json'
10.2. Request Fields
Path	Type	Description
email

String

user email (and login)

password

String

password

name

String

given name)

surname

String

family name

10.3. Response Fields
Path	Type	Description
login

String

user login

connectedToLdap

Boolean

is user account connected to LDAP

ldapAccountAvailable

Boolean

does the account exist in LDAP

active

Boolean

ist the use account active (can user login)

confirmed

Boolean

is the user email confirmed

email

String

email address

orcidId

String

orcid identifier

id

Number

user unique id

maxColor

color

color used for drawing data overlays with max value

minColor

color

color used for drawing data overlays with min value

neutralColor

color

color used for drawing data overlays with 0 value

simpleColor

color

color used for drawing data overlays without value

name

String

first name

surname

String

last name

removed

Boolean

is the account removed

termsOfUseConsent

Boolean

did user agree to terms of use

privileges

Array

list of user privileges

privileges[].objectId

String

object id to which project has privilege

lastActive

String

datetime of the last activity in the active session

privileges[].privilegeType

String

type of privilege, available values: IS_ADMIN, IS_CURATOR, READ_PROJECT, WRITE_PROJECT

10.4. Sample Response
{
  "id" : 823,
  "login" : "piotr.gawron@uni.lu",
  "name" : "Piotr",
  "surname" : "Gawron",
  "email" : "piotr.gawron@uni.lu",
  "orcidId" : null,
  "minColor" : null,
  "maxColor" : null,
  "neutralColor" : null,
  "simpleColor" : null,
  "removed" : false,
  "connectedToLdap" : false,
  "termsOfUseConsent" : false,
  "privileges" : [ {
    "privilegeType" : "READ_PROJECT",
    "objectId" : "empty"
  } ],
  "active" : false,
  "confirmed" : false,
  "ldapAccountAvailable" : false,
  "lastActive" : null
}
11. Confirm email
11.1. CURL sample
$ curl 'https://minerva-service.lcsb.uni.lu/minerva/api/users/test_user:confirmEmail' -X POST \
    -d 'token=b86bd30b-f8bb-4803-9a42-44f40d3dd3fa' \
    -H 'Content-Type: application/x-www-form-urlencoded'
11.2. Request Parameters
Parameter	Description
token

token obtained in the registration email

11.3. Path Parameters
Table 8. /minerva/api/users/{login}:confirmEmail
Parameter	Description
login

user login

11.4. Response Fields
Path	Type	Description
message

String

detailed information about the status

status

String

status

11.5. Sample Response
{
  "message" : "Your email is confirmed. You need to wait for admin approval before you can login",
  "status" : "OK"
}
Version 18.2.1 2025-04-24T11:05:57Z
Last updated 2025-04-24 04:48:53 UTC
