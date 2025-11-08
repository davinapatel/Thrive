import Home from "./page/Home";
import Header from "./components/Header"
import { Routes, Route } from "react-router-dom";
import "./App.css"

function App() {

    return (
        <>
        <div className="d-flex flex-column min-vh-100">
            <Header />
                <Routes>
                    <Route path = "/" element = {<Home />} />
                </Routes>
            
        </div>
        </>
    );
}

export default App;