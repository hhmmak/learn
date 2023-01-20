import Todo from './component/Todo';
import './App.css';

function App() {

  
  const todos =[
    {id: 1, title: 'wash dishes', completed: false},
    {id: 2, title: 'do laundry', completed: true},
  ];

  return (
    <div className="App">
      { todos.map((item) => 
        <Todo item={item} />
      )}
    </div>
  );
}

export default App;
