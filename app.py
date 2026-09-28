
[     UTC     ] Logs for biowatch-setif-dycgdj2roytbfexymndpwf.streamlit.app/
────────────────────────────────────────────────────────────────────────────────────────
[13:41:52] 🚀 Starting up repository: 'biowatch-setif', branch: 'main', main module: 'app.py'
[13:41:52] 🐙 Cloning repository...
[13:41:53] 🐙 Cloning into '/mount/src/biowatch-setif'...

[13:41:53] 🐙 Cloned repository!
[13:41:53] 🐙 Pulling code changes from Github...
[13:41:54] 📦 Processing dependencies...

──────────────────────────────────────── uv ───────────────────────────────────────────

Using uv pip install.
Using Python 3.14.7 environment at /home/adminuser/venv
Resolved 61 packages in 1.11s
Prepared 61 packages in 1.84s
Installed 61 packages in 111ms
 + altair==6.3.0
 + annotated-types==0.8.0
 + anyio==4.15.1
 + attrs==26.1.0
 [2026-09-23 13:41:57.470973] + certifi==2026.7.22
 + cffi==2.1.1[2026-09-23 13:41:57.471270] 
 + charset-normalizer==3.5.1
 +[2026-09-23 13:41:57.471552]  click==8.5.0
 + cryptography==[2026-09-23 13:41:57.471892] 50.0.1
 + deprecation==2.1.0[2026-09-23 13:41:57.472095] 
 + h11==0.16.0
 + h2[2026-09-23 13:41:57.472468] ==4.4.1
 + hpack==4.2.0[2026-09-23 13:41:57.472683] 
 + httpcore==1.0.9
 [2026-09-23 13:41:57.472871] + httptools==0.8.0
 + httpx[2026-09-23 13:41:57.473038] ==0.28.1
 + hyperframe==6.1.0[2026-09-23 13:41:57.473205] 
 + idna==3.20
 +[2026-09-23 13:41:57.473447]  itsdangerous==2.2.0
 + jinja2[2026-09-23 13:41:57.473644] ==3.1.6
 + jsonschema==4.26.0[2026-09-23 13:41:57.473840] 
 + jsonschema-specifications==2025.9.1
 +[2026-09-23 13:41:57.474027]  markupsafe==3.0.3[2026-09-23 13:41:57.474202] 
 + multidict==6.9.1
 [2026-09-23 13:41:57.474489] + narwhals==2.26.0
 + numpy[2026-09-23 13:41:57.474742] ==2.5.3
 + packaging==26.3[2026-09-23 13:41:57.475005] 
 + pandas==3.0.6
 + pillow==12.3.0
 + postgrest==2.31.0
 + propcache==0.5.4
 + protobuf==7.36.2
 + pyarrow==25.0.1[2026-09-23 13:41:57.475188] 
 + pycparser==3.0
 + pydantic==2.13.5
 + pydantic-core==2.46.5
 + pydeck==0.9.3
 + pyjwt==2.14.0
 + python-dateutil==2.9.0.post0
 + python-multipart==0.0.32
 + realtime==2.31.0
 + referencing==0.37.0
 + requests==2.34.2
 + rpds-py==2026.6.3
 [2026-09-23 13:41:57.475457] + six==1.17.0
 + st-supabase-connection==2.2.1
 + starlette==1.7.0
 + storage3==2.31.0
 + streamlit==1.64.0
 + strenum==0.4.15
 + supabase==2.31.0
 + supabase-auth==2.31.0
 + supabase-functions==2.31.0
 + toml==0.10.2
 + typing-extensions==4.16.0
 + typing-inspection==0.4.4
 + urllib3==2.8.0
 + uvicorn==0.53.0
 + watchdog==6.0.0
 + websockets==15.0.1
 + yarl==[2026-09-23 13:41:57.475874] 1.25.1
Checking if Streamlit is installed
Found Streamlit version 1.64.0 in the environment
Detected pyarrow 25.0.1 (known segfault, apache/arrow#50471). Replacing with pyarrow<25.
Using uv pip install.
Using Python 3.14.7 environment at /home/adminuser/venv
Resolved 1 package in 37ms
Prepared 1 package in 699ms
Uninstalled 1 package in 17ms
Installed 1 package in 21ms
 - pyarrow==25.0.1
 + pyarrow==24.0.0
Installing rich for an improved exception logging
Using uv pip install.
Using Python 3.14.7 environment at /home/adminuser/venv
Resolved 4 packages in 162ms
Prepared 4 packages in 139ms
Installed 4 packages in 12ms
 + markdown-it-py==4.2.0
 + mdurl==0.1.2[2026-09-23 13:42:02.264750] 
 + pygments==2.21.0
 + rich==15.0.0

────────────────────────────────────────────────────────────────────────────────────────

[13:42:02] 🐍 Python dependencies were installed from /mount/src/biowatch-setif/requirements.txt using uv.
Check if streamlit is installed
Streamlit is already installed
[13:42:04] 📦 Processed dependencies!
2026-09-23 13:42:05.776 Uvicorn server started on :::8501



────────────────────── Traceback (most recent call last) ───────────────────────
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:136 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:909 in code_to_exec                                     
                                                                                
  /mount/src/biowatch-setif/app.py:24 in <module>                               
                                                                                
     21 # SUPABASE CONNECTION                                                   
     22 # =========================                                             
     23                                                                         
  ❱  24 conn = st.connection(                                                   
     25 │   "supabase",                                                         
     26 │   type=SupabaseConnection                                             
     27 )                                                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:475 in connection_factory                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_  
  util.py:725 in wrapped_func                                                   
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:124 in _create_connection                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:705 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:761 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:823 in _handle_cache_miss                                      
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:87 in __create_connection                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/connections/base  
  _connection.py:80 in __init__                                                 
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/st_supabase_connection/__i  
  nit__.py:211 in _connect                                                      
                                                                                
    208 │   │                                                                   
    209 │   │   self._url = url                                                 
    210 │   │   self._key = key                                                 
  ❱ 211 │   │   self.client = create_client(self._url, self._key)               
    212 │   │   self.table = self.client.table                                  
    213 │   │   self._shared_auth = self.client.auth                            
    214 │   │   self.delete_bucket = self.client.storage.delete_bucket          
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:3  
  80 in create_client                                                           
                                                                                
    377 │   -------                                                             
    378 │   Client                                                              
    379 │   """                                                                 
  ❱ 380 │   return Client.create(                                               
    381 │   │   supabase_url=supabase_url, supabase_key=supabase_key, options=  
    382 │   )                                                                   
    383                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:1  
  09 in create                                                                  
                                                                                
    106 │   │   options: Optional[ClientOptions] = None,                        
    107 │   ) -> "Client":                                                      
    108 │   │   auth_header = options.headers.get("Authorization") if options   
  ❱ 109 │   │   client = cls(supabase_url, supabase_key, options)               
    110 │   │                                                                   
    111 │   │   if auth_header is None:                                         
    112 │   │   │   try:                                                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:6  
  3 in __init__                                                                 
                                                                                
     60 │   │                                                                   
     61 │   │   # Check if the url and key are valid                            
     62 │   │   if not re.match(r"^(https?)://.+", supabase_url):               
  ❱  63 │   │   │   raise SupabaseException("Invalid URL")                      
     64 │   │                                                                   
     65 │   │   if options is None:                                             
     66 │   │   │   options = ClientOptions(storage=SyncMemoryStorage())        
────────────────────────────────────────────────────────────────────────────────
SupabaseException: Invalid URL
────────────────────── Traceback (most recent call last) ───────────────────────
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:136 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:909 in code_to_exec                                     
                                                                                
  /mount/src/biowatch-setif/app.py:24 in <module>                               
                                                                                
     21 # SUPABASE CONNECTION                                                   
     22 # =========================                                             
     23                                                                         
  ❱  24 conn = st.connection(                                                   
     25 │   "supabase",                                                         
     26 │   type=SupabaseConnection                                             
     27 )                                                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:475 in connection_factory                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_  
  util.py:725 in wrapped_func                                                   
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:124 in _create_connection                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:705 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:761 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:823 in _handle_cache_miss                                      
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:87 in __create_connection                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/connections/base  
  _connection.py:80 in __init__                                                 
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/st_supabase_connection/__i  
  nit__.py:211 in _connect                                                      
                                                                                
    208 │   │                                                                   
    209 │   │   self._url = url                                                 
    210 │   │   self._key = key                                                 
  ❱ 211 │   │   self.client = create_client(self._url, self._key)               
    212 │   │   self.table = self.client.table                                  
    213 │   │   self._shared_auth = self.client.auth                            
    214 │   │   self.delete_bucket = self.client.storage.delete_bucket          
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:3  
  80 in create_client                                                           
                                                                                
    377 │   -------                                                             
    378 │   Client                                                              
    379 │   """                                                                 
  ❱ 380 │   return Client.create(                                               
    381 │   │   supabase_url=supabase_url, supabase_key=supabase_key, options=  
    382 │   )                                                                   
    383                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:1  
  09 in create                                                                  
                                                                                
    106 │   │   options: Optional[ClientOptions] = None,                        
    107 │   ) -> "Client":                                                      
    108 │   │   auth_header = options.headers.get("Authorization") if options   
  ❱ 109 │   │   client = cls(supabase_url, supabase_key, options)               
    110 │   │                                                                   
    111 │   │   if auth_header is None:                                         
    112 │   │   │   try:                                                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:6  
  3 in __init__                                                                 
                                                                                
     60 │   │                                                                   
     61 │   │   # Check if the url and key are valid                            
     62 │   │   if not re.match(r"^(https?)://.+", supabase_url):               
  ❱  63 │   │   │   raise SupabaseException("Invalid URL")                      
     64 │   │                                                                   
     65 │   │   if options is None:                                             
     66 │   │   │   options = ClientOptions(storage=SyncMemoryStorage())        
────────────────────────────────────────────────────────────────────────────────
SupabaseException: Invalid URL
────────────────────── Traceback (most recent call last) ───────────────────────
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:136 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:909 in code_to_exec                                     
                                                                                
  /mount/src/biowatch-setif/app.py:24 in <module>                               
                                                                                
     21 # SUPABASE CONNECTION                                                   
     22 # =========================                                             
     23                                                                         
  ❱  24 conn = st.connection(                                                   
     25 │   "supabase",                                                         
     26 │   type=SupabaseConnection                                             
     27 )                                                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:475 in connection_factory                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_  
  util.py:725 in wrapped_func                                                   
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:124 in _create_connection                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:705 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:761 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:823 in _handle_cache_miss                                      
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:87 in __create_connection                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/connections/base  
  _connection.py:80 in __init__                                                 
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/st_supabase_connection/__i  
  nit__.py:211 in _connect                                                      
                                                                                
    208 │   │                                                                   
    209 │   │   self._url = url                                                 
    210 │   │   self._key = key                                                 
  ❱ 211 │   │   self.client = create_client(self._url, self._key)               
    212 │   │   self.table = self.client.table                                  
    213 │   │   self._shared_auth = self.client.auth                            
    214 │   │   self.delete_bucket = self.client.storage.delete_bucket          
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:3  
  80 in create_client                                                           
                                                                                
    377 │   -------                                                             
    378 │   Client                                                              
    379 │   """                                                                 
  ❱ 380 │   return Client.create(                                               
    381 │   │   supabase_url=supabase_url, supabase_key=supabase_key, options=  
    382 │   )                                                                   
    383                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:1  
  09 in create                                                                  
                                                                                
    106 │   │   options: Optional[ClientOptions] = None,                        
    107 │   ) -> "Client":                                                      
    108 │   │   auth_header = options.headers.get("Authorization") if options   
  ❱ 109 │   │   client = cls(supabase_url, supabase_key, options)               
    110 │   │                                                                   
    111 │   │   if auth_header is None:                                         
    112 │   │   │   try:                                                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:6  
  3 in __init__                                                                 
                                                                                
     60 │   │                                                                   
     61 │   │   # Check if the url and key are valid                            
     62 │   │   if not re.match(r"^(https?)://.+", supabase_url):               
  ❱  63 │   │   │   raise SupabaseException("Invalid URL")                      
     64 │   │                                                                   
     65 │   │   if options is None:                                             
     66 │   │   │   options = ClientOptions(storage=SyncMemoryStorage())        
────────────────────────────────────────────────────────────────────────────────
SupabaseException: Invalid URL
────────────────────── Traceback (most recent call last) ───────────────────────
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:136 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:909 in code_to_exec                                     
                                                                                
  /mount/src/biowatch-setif/app.py:24 in <module>                               
                                                                                
     21 # SUPABASE CONNECTION                                                   
     22 # =========================                                             
     23                                                                         
  ❱  24 conn = st.connection(                                                   
     25 │   "supabase",                                                         
     26 │   type=SupabaseConnection                                             
     27 )                                                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:475 in connection_factory                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_  
  util.py:725 in wrapped_func                                                   
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:124 in _create_connection                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:705 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:761 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/caching/  
  cache_utils.py:823 in _handle_cache_miss                                      
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/connecti  
  on_factory.py:87 in __create_connection                                       
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/streamlit/connections/base  
  _connection.py:80 in __init__                                                 
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/st_supabase_connection/__i  
  nit__.py:211 in _connect                                                      
                                                                                
    208 │   │                                                                   
    209 │   │   self._url = url                                                 
    210 │   │   self._key = key                                                 
  ❱ 211 │   │   self.client = create_client(self._url, self._key)               
    212 │   │   self.table = self.client.table                                  
    213 │   │   self._shared_auth = self.client.auth                            
    214 │   │   self.delete_bucket = self.client.storage.delete_bucket          
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:3  
  80 in create_client                                                           
                                                                                
    377 │   -------                                                             
    378 │   Client                                                              
    379 │   """                                                                 
  ❱ 380 │   return Client.create(                                               
    381 │   │   supabase_url=supabase_url, supabase_key=supabase_key, options=  
    382 │   )                                                                   
    383                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:1  
  09 in create                                                                  
                                                                                
    106 │   │   options: Optional[ClientOptions] = None,                        
    107 │   ) -> "Client":                                                      
    108 │   │   auth_header = options.headers.get("Authorization") if options   
  ❱ 109 │   │   client = cls(supabase_url, supabase_key, options)               
    110 │   │                                                                   
    111 │   │   if auth_header is None:                                         
    112 │   │   │   try:                                                        
                                                                                
  /home/adminuser/venv/lib/python3.14/site-packages/supabase/_sync/client.py:6  
  3 in __init__                                                                 
                                                                                
     60 │   │                                                                   
     61 │   │   # Check if the url and key are valid                            
     62 │   │   if not re.match(r"^(https?)://.+", supabase_url):               
  ❱  63 │   │   │   raise SupabaseException("Invalid URL")                      
     64 │   │                                                                   
     65 │   │   if options is None:                                             
     66 │   │   │   options = ClientOptions(storage=SyncMemoryStorage())        
────────────────────────────────────────────────────────────────────────────────
SupabaseException: Invalid URL
