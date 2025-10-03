#!/usr/bin/env python3
"""
borough_complaints.py - CLI tool for analyzing NYC 311 complaints by borough

This script analyzes NYC 311 Service Request data and outputs the count of 
complaint types per borough within a specified date range.
"""

import argparse
import csv
import sys
from datetime import datetime
from collections import defaultdict


def parse_date(date_str):
    """
    Parse date string in format MM/DD/YYYY HH:MM:SS AM/PM to datetime object.
    
    Args:
        date_str: Date string from CSV file
        
    Returns:
        datetime object or None if parsing fails
    """
    try:
        return datetime.strptime(date_str, '%m/%d/%Y %I:%M:%S %p')
    except (ValueError, AttributeError):
        return None


def filter_complaints(input_file, start_date, end_date):
    """
    Filter complaints by date range and count by complaint type and borough.
    
    Args:
        input_file: Path to input CSV file
        start_date: Start date as datetime object
        end_date: End date as datetime object
        
    Returns:
        Dictionary with (complaint_type, borough) as keys and counts as values
    """
    complaint_counts = defaultdict(int)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                # Get the created date
                created_date_str = row.get('Created Date', '')
                created_date = parse_date(created_date_str)
                
                # Skip if date parsing failed or date is outside range
                if not created_date:
                    continue
                if created_date < start_date or created_date > end_date:
                    continue
                
                # Get complaint type and borough
                complaint_type = row.get('Complaint Type', '').strip()
                borough = row.get('Borough', '').strip()
                
                # Skip if either field is empty
                if not complaint_type or not borough:
                    continue
                
                # Increment count
                complaint_counts[(complaint_type, borough)] += 1
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    return complaint_counts


def output_results(complaint_counts, output_file=None):
    """
    Output results in CSV format.
    
    Args:
        complaint_counts: Dictionary with (complaint_type, borough) keys and counts
        output_file: Optional output file path. If None, print to stdout.
    """
    # Sort by complaint type, then borough for consistent output
    sorted_items = sorted(complaint_counts.items(), key=lambda x: (x[0][0], x[0][1]))
    
    # Prepare output
    output_lines = ['complaint type, borough, count']
    for (complaint_type, borough), count in sorted_items:
        output_lines.append(f'{complaint_type}, {borough}, {count}')
    
    # Write to file or stdout
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output_lines) + '\n')
        except Exception as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print('\n'.join(output_lines))


def main():
    """Main function to parse arguments and run the analysis."""
    parser = argparse.ArgumentParser(
        description='Analyze NYC 311 complaints by borough and complaint type for a given date range.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -i data.csv -s 01/01/2024 -e 01/31/2024
  %(prog)s -i data.csv -s 01/01/2024 -e 01/31/2024 -o results.csv
  
Date format: MM/DD/YYYY
        """
    )
    
    parser.add_argument(
        '-i', '--input',
        required=True,
        metavar='<input file>',
        help='Input CSV file containing 311 service requests'
    )
    
    parser.add_argument(
        '-s', '--start',
        required=True,
        metavar='<start date>',
        help='Start date in MM/DD/YYYY format'
    )
    
    parser.add_argument(
        '-e', '--end',
        required=True,
        metavar='<end date>',
        help='End date in MM/DD/YYYY format'
    )
    
    parser.add_argument(
        '-o', '--output',
        metavar='<output file>',
        help='Output CSV file (if not specified, prints to stdout)'
    )
    
    args = parser.parse_args()
    
    # Parse start and end dates
    try:
        start_date = datetime.strptime(args.start, '%m/%d/%Y')
        end_date = datetime.strptime(args.end, '%m/%d/%Y')
        # Set end date to end of day
        end_date = end_date.replace(hour=23, minute=59, second=59)
    except ValueError:
        print("Error: Dates must be in MM/DD/YYYY format", file=sys.stderr)
        sys.exit(1)
    
    # Validate date range
    if start_date > end_date:
        print("Error: Start date must be before or equal to end date", file=sys.stderr)
        sys.exit(1)
    
    # Process complaints
    complaint_counts = filter_complaints(args.input, start_date, end_date)
    
    # Output results
    output_results(complaint_counts, args.output)


if __name__ == '__main__':
    main()

