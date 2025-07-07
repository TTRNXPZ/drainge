const data = {
    index: "test"
}

const url = 'https://sensor.sjp-gis.com/v2/sensor/receiver'

const test = async () => {
    const respone = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY3Rpb24iOiJub2l0ZnkiLCJpYXQiOjE3NDA0NzAwMzZ9.V56j-FyQ68GkOtwXdpeqcWD0SfDCbIz6yNral7WUTvM"
        },
        body: JSON.stringify(data),
    })


console.log(respone)

}

test()