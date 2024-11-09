from xrpl.client import Client 

networks = {
    RIPPLE_TESTNET: "wss://s.altnet.rippletest.net:51233"
}

client
export const getClient = () => {
    if(!client) {
        client = new Client(networks.RIPPLE_TESTNET)
    }

    return client
}