export default {
    connectionSocket ({state, commit}, path) {
        const socket = new WebSocket(path)
        commit("setSocket", socket)
    },
    connectionMessageSocket ({state, commit}, path) {
        const socket = new WebSocket(path)
        commit("setMessageSocket", socket)
    },
    open ({state,commit}, success) {
        state.socket.onopen  = () => {
            console.log('已连接');
            success && success();
        },
        state.messageSocket.onopen = () => {
            console.log('8766已连接')
        } 
    },
    wsError ({state, commit}, fail) {
        state.socket.onerror  = () => {
            console.log('连接错误');
            fail && fail();
        },
        state.messageSocket.onerror = () => {
            console.log('8766连接错误')
        }
    },
    getMessage ({state, commit}) {
        console.log('发消息');
        state.messageSocket.onmessage = (msg) => {
            // console.log(msg.data);
            commit('setMessage', msg.data);
        }
    },
    send ({state, commit}, conditions) {
        state.socket.send(conditions)
    },
    close ({state, commit},socketClose) {
        state.socket.onclose = () => {
            console.log('已关闭');
            // commit('setIsClose', true)
            // socketClose && socketClose()
        },
        state.messageSocket.onclose = () => {
            console.log('8766已关闭')
        }
    },
    closeSocket ({state, commit}) {
        state.socket.close()
    },
    setSendData ({state, commit}, name, value) {
        if (name == 'TL' || name == 'CD') {
            commit('setSendData', name, value);
        }else {
            commit('setSendData', name);
        }
        
    },
    changeColor ({state, commit},color) {
        commit('setColor', color)
    }
}