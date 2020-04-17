export default {
    setSocket (state, socket) {
        state.socket = socket;
    },
    setMessageSocket(state, socket) {
        state.messageSocket = socket
    },
    setMessage(state, message) {
        console.log(message);
        state.msg = message
    },
    setSendData (state,name) {
        state.sendDatas[name]
    },
    setColor (state, color) {
        state.color = color
    },
    setLine (state, line) {
        state.line = line
    },
    setCliff (state, cliff) {
        state.cliff = cliff
    },
    setIsClose (state, isClose) {
        state.isClose = isClose
    }
}