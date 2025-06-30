# Code block data structures

from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field

@dataclass
class CodeBlock:
    content: str
    language: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)
    placeholder: Optional[str] = None

@dataclass
class ProcessingContext:
    placeholder_map: Dict[str, CodeBlock] = field(default_factory=dict)
    state: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ConversionResult:
    html: str
    code_blocks: Dict[str, str] = field(default_factory=dict)
    success: bool = True
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
