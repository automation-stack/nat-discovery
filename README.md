## Cross-platform NAT behavior discovery (algorithms defined in RFC 3489) 

<a href="http://www.netmanias.com/en/post/techdocs/6066/nat-stun/nat-behavior-discovery-using-classic-stun-rfc-3489">NAT Behavior Discovery Using Classic STUN (RFC 3489)</a>

- Test II checks the presence of a NAT or symmetric UDP firewall, and discovers a full cone NAT
- Test I' discovers a symmetric NAT
- Test III discovers a restricted con NAT or port restricted cone NAT

<img style="vertical-align:top" width="45%" src="http://www.netmanias.com/en/?m=attach&no=3603" />
<img width="50%"src="http://g.recordit.co/RwB5sDZt89.gif" />

### Configuration

```
> nat-discovery --help

usage: nat-discovery [-h] [-d] [-j] [-e] [-H STUN_HOST] [-P STUN_PORT] [-i SOURCE_IP] [-p SOURCE_PORT] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           enable debug logging (default: False)
  -j, --json            JSON output (default: False)
  -e, --exit            exit on complete (by default sleep) (default: False)
  -H STUN_HOST, --stun-host STUN_HOST
                        STUN host to use (default: None)
  -P STUN_PORT, --stun-port STUN_PORT
                        STUN host port to use (default: 3478)
  -i SOURCE_IP, --source-ip SOURCE_IP
                        network interface for client (default: 0.0.0.0)
  -p SOURCE_PORT, --source-port SOURCE_PORT
                        port to listen on for client (default: 54320)
  --version             show program's version number and exit

```
