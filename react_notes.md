
```jsx
import './styles.css';
import {useState,useEffect} from "react"
const Li = ({todo,deleteTodo})=>{
  return (<li key={todo}>
          <span>{todo}</span>
          <button onClick={()=>deleteTodo(todo)}>Delete</button>
        </li>)
}
export default function App() {
  const [newTodo,setNewTodo] = useState("")
  const [todos,setTodos] = useState([])

  const deleteTodo = (todo)=>{
   tds = todos.filter((td)=>td!=todo)
   setTodos(tds)
 
   
  }
  const addTodo = (e)=>{
    e.preventDefault()
    if (!newTodo){
      alert("Todo cannot be empty")
      return
    }
    setTodos([newTodo,...todos])
    setNewTodo("")

  }
  return (
    <div>
      <h1>Todo List</h1>
      <div>
        <input type="text" value={newTodo} placeholder="Add your task" onChange={(e)=>setNewTodo(e.target.value)} />
        <div>
          <button onClick={addTodo}>Submit</button>
        </div>
      </div>
      <ul>
      {todos?.map((todo) => (<Li todo={todo} deleteTodo={deleteTodo}/>))}
       
        
      </ul>
    </div>
  );
}
```
