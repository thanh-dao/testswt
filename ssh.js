const fs = require('fs');
const path = require('path');
const {NodeSSH} = require('node-ssh');
const ssh = new NodeSSH();

ssh.connect({
    host: '27.64.30.83',
    username: 'thanh',
    port: 6767,
    password: "1509",
    tryKeyboard: true,
  })
.then(function() {
    ssh.execCommand("echo 123");
});