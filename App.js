"use client"

import React from "react"
import AuthPage from "./AuthPage"
import SettingsPage from "./SettingsPage"
import FeedbackPage from "./FeedbackPage"
import CameraPage from "./CameraPage"
import ChatInterface from "./ChatInterface"
import Sidebar from "./Sidebar"
import ToastProvider from "./ToastProvider"

function App() {
  const [isAuthenticated, setIsAuthenticated] = React.useState(false)
  const [isLoading, setIsLoading] = React.useState(true)
  const [currentPage, setCurrentPage] = React.useState("chat")

  React.useEffect(() => {
    // Check if user is authenticated
    const token = localStorage.getItem("gs-ai-token")
    if (token) {
      setIsAuthenticated(true)
    }
    setIsLoading(false)
  }, [])

  const handleLogout = () => {
    localStorage.removeItem("gs-ai-token")
    setIsAuthenticated(false)
  }

  if (isLoading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary"></div>
      </div>
    )
  }

  if (!isAuthenticated) {
    return (
      <ToastProvider>
        <AuthPage onAuth={() => setIsAuthenticated(true)} />
      </ToastProvider>
    )
  }

  const renderContent = () => {
    switch (currentPage) {
      case "settings":
        return <SettingsPage />
      case "feedback":
        return <FeedbackPage />
      case "camera":
        return <CameraPage />
      default:
        return <ChatInterface />
    }
  }

  return (
    <ToastProvider>
      <div className="min-h-screen bg-background flex">
        <Sidebar currentPage={currentPage} onPageChange={setCurrentPage} onLogout={handleLogout} />
        <div className="flex-1 chat-container">{renderContent()}</div>
      </div>
    </ToastProvider>
  )
}
