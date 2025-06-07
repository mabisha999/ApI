
import { useState,useEffect } from "react"



import Menu from './Menu.jsx'

function Button(){
const [isEditing,setIsEditing]=useState(false)
const [userData, setUserData] = useState(null);
const [userData1, setUserData1] = useState(null);
const [userData2, setUserData2] = useState(null);
const [userData3, setUserData3] = useState(null);

const [title,setTitle] =useState()
const [url,seturl]=useState()
const [cap ,setcap]=useState()
const sendData=(e)=>{
    fetch('http://127.0.0.1:8000/Api3', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',

  },
  body: JSON.stringify({
    title: title,
    url: url,
    caption:cap
  })
})

}

    useEffect(() => {

 fetch("http://127.0.0.1:8000/page1")
            .then((res) => res.json())
            .then((json) => {
              console.log(json)
                setUserData(json[0])
                setUserData1(json);
               
            });
        },[]);

    useEffect(() => {

 fetch("http://127.0.0.1:8000/page2")
            .then((res) => res.json())
            .then((json) => {
                console.log(json)
                setUserData2(json);
               
            });

        },[]);
      useEffect(() => {
 fetch("http://127.0.0.1:8000/Api4")
 .then((res) => res.json())
            .then((json) => {
               console.log(json)
                
                setUserData3(json);
               
            }); 
             },[]);     
      

      
    useEffect(() => {
console.log(userData1);
    },[userData1]);
    useEffect(() => {
console.log(userData2);
    }, [userData2]);

      useEffect(() => {
console.log(userData3);
    }, [userData3]);
      
      

          
      
const hideTodo=()=>{
        setIsEditing(!isEditing)  
}    
return(
<>
<Menu></Menu>
<div className="but">
          
    <div className="but1"> 
        <div>
            <h2>BankDetails</h2>
                            {userData2 && (
          
               
      <p> name: {userData2.name}<br></br>
                
                    accountNumber: {userData2.accountNumber}<br></br>
                    balance: {userData2.balance}</p>

                )
            }
           
            </div>  
            <div>
                <h3>api3</h3>
                <input
                type="text"
                value={title}
                placeholder="title"
                onChange={(e)=> setTitle(e.target.value)}
                
                />
                <br></br>
                                
                <input
                type="text"
                
                value={url}
                placeholder="url"
                onChange={(e)=> seturl(e.target.value)}
                
                
                />
                 <br></br>               
                <input
                type="text"
                value={cap}
                placeholder="  caption"
                onChange={(e)=> setcap(e.target.value)}
                
                />
                <br></br>
                <button onClick={sendData}>submit</button>
                <p>
                    title:{title}<br></br>
                    url:{url}<br></br>
                    caption:{cap}
                </p>
                
                </div>        
                 <div>  <h2>products</h2>
                 
                    
                {userData && (
          
               
    <p>             id: {userData.name}<br></br>
                    city: {userData.city}<br></br>
                    description:{userData.startedIn}</p>

                )
            }
            </div>
            </div>
      <div>
        {
            userData1 && userData1.map((item)=>{
                return (
                    <div className="pro">
                 <p>id:{item.name}</p>       
                <p>age:{item.age}</p>
                <p>city:{item.city}</p>
                <p>{item.startedIn}</p>
                </div>
                )
            }
        )}
        {
             userData3 && userData3.map((item)=>{
                return (
                    <div className="pro">
                 <p>title:{item.title}</p>       
                <p>url:{item.url}</p>
                <p>caption:{item.caption}</p>
                
                </div>
                )
             }
            )
}


        </div>        
      
        </div>
<div className="bu">
 <p style={{display:isEditing?'none':'block'}}> Arunachala College of Engineering for Women at Kanyakumari ranks No.1 <br></br>
     all engineering college in Tamil Nadu based on Anna University Results<br></br>.
     Arunachala College offer various MCA, MBA, UG, PG and<br></br>
     Research programs in Engineering and Technology.
 </p>
     <button onClick={hideTodo}>{isEditing?'show':'Hide'}</button>
   </div> 
    </>
)
}
export default Button