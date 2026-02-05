"""
Integration tests for the CLI functionality.
"""

import sys
from io import StringIO
from unittest.mock import patch
from src.main import main


class TestCLIIntegration:
    """Integration tests for the CLI commands."""

    def test_add_and_list_todos(self):
        """Test adding a todo and then listing it."""
        # Test add command
        test_args = ['todo', 'add', 'Test', 'task', '--priority', 'high']

        with patch.object(sys, 'argv', test_args):
            # Capture stdout
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):  # Suppress any error messages
                    try:
                        main()
                    except SystemExit:
                        pass  # Expected after argument parsing

            output = captured_output.getvalue()
            assert "Todo #1 added: Test task (Priority: High)" in output

    def test_add_complete_and_list_todos(self):
        """Test adding a todo, completing it, and verifying the status."""
        # First, add a todo
        test_args = ['todo', 'add', 'Test', 'task']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

        # Then, complete the todo
        test_args = ['todo', 'complete', '1']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

            output = captured_output.getvalue()
            assert "Todo #1 marked as completed" in output

    def test_add_delete_and_verify(self):
        """Test adding a todo, deleting it, and verifying it's gone."""
        # First, add a todo
        test_args = ['todo', 'add', 'Test', 'to', 'delete']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

        # Then, delete the todo
        test_args = ['todo', 'delete', '1']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

            output = captured_output.getvalue()
            assert "Todo #1 deleted" in output

    def test_search_functionality(self):
        """Test searching for todos by keyword."""
        # First, add a todo with a specific keyword
        test_args = ['todo', 'add', 'Buy', 'groceries', 'for', 'the', 'week']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

        # Then, search for the keyword
        test_args = ['todo', 'search', 'groceries']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

            output = captured_output.getvalue()
            assert "groceries" in output
            assert "Buy groceries for the week" in output

    def test_list_command_filters(self):
        """Test the list command with different filters."""
        # Add a few todos
        test_args = ['todo', 'add', 'Pending', 'task']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

        test_args = ['todo', 'add', 'Completed', 'task']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

        # Complete the second task
        test_args = ['todo', 'complete', '2']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

        # Test list with 'pending' filter
        test_args = ['todo', 'list', 'pending']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

            output = captured_output.getvalue()
            assert "Pending" in output
            assert "Completed" not in output

        # Test list with 'completed' filter
        test_args = ['todo', 'list', 'completed']

        with patch.object(sys, 'argv', test_args):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                with patch('sys.stderr', StringIO()):
                    try:
                        main()
                    except SystemExit:
                        pass

            output = captured_output.getvalue()
            assert "Completed" in output
            assert "Pending" not in output