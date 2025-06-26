import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './index.css';
import Login from './pages/Login.tsx';
import Register from './pages/Register.tsx';
import Dashboard from './pages/Dashboard.tsx';
import UserSettings from "./pages/UserSettings";


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/settings" element={<UserSettings />} />
        <Route path='/dashboard' element={<Dashboard />}/>
        <Route path='/register' element={<Register />}/>
        <Route path='/login' element={<Login />}/>
      </Routes>
    </BrowserRouter>
  </StrictMode>
);
