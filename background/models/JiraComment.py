from dataclasses import dataclass

from dataclasses_json import dataclass_json

from background.models.JiraReporter import JiraReporter


@dataclass_json
@dataclass
class JiraComment:
    self: str
    author: JiraReporter
    body: str
