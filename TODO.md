# TODO
## Security
* Only allow private subnet NAT to access openAIs servers
  * Would need to add apt endpoints manually or manually reset the ingress rules whenever I want to update
* Encryption:
  * Need to encrypt the drives of proxy, backend, and cache hosts (Encryption at rest)
    * Create snapshots, new encrypted EBS volumes from snapshots, swap with original 
  * Need to change the protocol to HTTPS for: (Encryption in flight)
    * proxy => backend [DONE]
    * backend => redis 
  * Attach SSL cert to public domain, nginx already configured for HTTPS

## Testing
* Currently testing in place from the client side only, server side errors will be missed as long as the client gets a response from openAI. This should be okay in theory but there's been intermediate states where it would be better to fail the step due to server errors and it would fail earlier in many cases.
 
## Interface / Features
* React rewrite + face lift
* Implement and store chat history (maybe)
* Multiple sessions per API key
