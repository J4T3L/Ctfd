import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import SqliPage from './pages/SqliPage';
import SstiPage from './pages/SstiPage';
import IdorPage from './pages/IdorPage';
import LfiPage from './pages/LfiPage';
import RcePage from './pages/RcePage';
import SsrfPage from './pages/SsrfPage';
import XssPage from './pages/XssPage';
import JwtPage from './pages/JwtPage';
import LogicPage from './pages/LogicPage';
import PicklePage from './pages/PicklePage';
import CookiePage from './pages/CookiePage';
import RobotsPage from './pages/RobotsPage';

export default function App() {
  return (
    <BrowserRouter>
      <div className="app-layout">
        <Sidebar />
        <div className="main-content">
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/app/sqli" element={<SqliPage />} />
            <Route path="/app/ssti" element={<SstiPage />} />
            <Route path="/app/idor" element={<IdorPage />} />
            <Route path="/app/lfi" element={<LfiPage />} />
            <Route path="/app/rce" element={<RcePage />} />
            <Route path="/app/ssrf" element={<SsrfPage />} />
            <Route path="/app/xss" element={<XssPage />} />
            <Route path="/app/jwt" element={<JwtPage />} />
            <Route path="/app/logic" element={<LogicPage />} />
            <Route path="/app/pickle" element={<PicklePage />} />
            <Route path="/app/cookie" element={<CookiePage />} />
            <Route path="/app/robots" element={<RobotsPage />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
