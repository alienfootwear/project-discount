# project-discount


Build: docker-compose build

Run: docker-compose up 

Test that it works:
curl http://localhost:8888/api/campaign
should give you: 
{"results":[[1,1,"A great discount",100]]} 


