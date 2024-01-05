const delayAdd = index => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if ( index > 10 ){
                reject(`${index}는 10보다 클 수 없습니다`)
                return
            }
            console.log(index)
            resolve(index + 1)
        }, 1000)
    })
    
}
delayAdd(13)
    .then(res => console.log(res))
    .catch(err => console.err(err))

const wrap = async() =>{
    const res = await delayAdd(13);
    console.log(res)
}


wrap()