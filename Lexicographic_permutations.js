'use strict';
let result = ''
let output
let counter = 0
function permatiution(str,remaining=null) {
    if (str.length === 1) {
        output =  remaining + str
        remaining = remaining.replace(remaining[remaining.length-1],'')
        return output
    }
    for (let i = 0; i < str.length; i++) {
        if(counter < 999999){
            result += permatiution(str.replace(str[i],''),remaining ? remaining + str[i] : str[i]) 
            counter++
        }
        
    }
    return result
}
console.log(new Set(permatiution('0123456789').match(/.{1,10}/g)))


// '012' ''   '
// '12' '0'
// '2' '01'
// let str = '012'
// let output = str.substr(1) 
// console.log(str)
