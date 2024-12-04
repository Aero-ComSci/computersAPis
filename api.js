
//Issues with the following code due to CORS

// async function getData() {
//     const url = "https://cs-api.pltw.org/baezmatic";
//     try {
//       const response = await fetch(url, {
//         method: "GET",
//         mode: "no-cors",
//         headers: {
//                    'Accept-Encoding': 'identity' // Try this
//                }
//            });
    
//       if (!response.ok) {
//         throw new Error(`Response status: ${response.status}`);
//       }
  
//       const json = await response.json();
//       console.log(json);
//     } catch (error) {
//       console.error(error.message);
//     }
//   }


 