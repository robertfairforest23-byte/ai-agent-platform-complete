"""
MIKE Agent - Assistant Agent Implementation
Handles general questions and conversational tasks
"""

import logging
from typing import Any, Dict
from src.agents.base_agent import BaseAgent


class AssistantAgent(BaseAgent):
    """Agent for general assistance and conversations"""
    
    def __init__(self):
        super().__init__(
            name="AssistantAgent",
            description="General purpose assistant for answering questions and conversations"
        )
    
    async def process(self, command: str) -> Dict[str, Any]:
        """Process user command"""
        self.logger.info(f"Processing: {command}")
        
        # Provide helpful responses
        response = self._generate_response(command)
        
        return {
            'success': True,
            'response': response,
            'agent': self.name
        }
    
    def _generate_response(self, command: str) -> str:
        """Generate a helpful response"""
        command_lower = command.lower()
        
        # Simple pattern matching for common questions
        if 'hello' in command_lower or 'hi' in command_lower:
            return "👋 Hello! How can I help you today?"
        elif 'how are you' in command_lower:
            return "😊 I'm doing great! Ready to help you with anything."
        elif 'what is your name' in command_lower or 'who are you' in command_lower:
            return "🤖 I'm MIKE, your personal AI assistant!"
        elif 'thank' in command_lower:
            return "😊 You're welcome! Anything else I can help with?"
        elif 'time' in command_lower:
            return "Try 'Show all clocks' to see current time in multiple zones!"
        elif 'task' in command_lower or 'todo' in command_lower:
            return "Try 'Show tasks' to see your to-do list!"
        else:
            return f"I heard you say: '{command}'. This feature is still being developed. Try 'Help' for available commands!"
