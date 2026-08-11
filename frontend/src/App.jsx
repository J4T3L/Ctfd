import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import ToolsPage from './pages/ToolsPage';
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
import WeakHashPage from './pages/WeakHashPage';
import XxePage from './pages/XxePage';
import CommentPage from './pages/CommentPage';

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
            <Route path="/app/tools" element={<ToolsPage />} />
            <Route path="/app/sqli" element={<SqliPage />} />
            <Route path="/app/comment" element={<CommentPage />} />
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
            <Route path="/app/weak_hash" element={<WeakHashPage />} />
            <Route path="/app/xxe" element={<XxePage />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
