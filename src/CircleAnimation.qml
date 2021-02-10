import QtQuick 2.0
import QtQml.Models 2.2

Item {

    DelegateModel {
        id: circlesViewModel
        model: manager.circlesModel
        delegate:
            NoteCircle {
                text: noteName
            }
    }

//    PathView {
//        anchors.fill: parent
//        model: circlesViewModel
//        path: Path {

//                  startX: 188; startY: 420

//                  PathArc {
//                      x: 266; y: 382
//                      radiusX: 100; radiusY: 100
//                  }
//                  PathArc {
//                      x: 285; y: 298
//                      radiusX: 100; radiusY: 100
//                  }
//                  PathArc {
//                      x: 231; y: 230
//                      radiusX: 100; radiusY: 100
//                  }
//                  PathArc {
//                      x: 144; y: 230
//                      radiusX: 100; radiusY: 100
//                  }
//                  PathArc {
//                      x: 90; y: 298
//                      radiusX: 100; radiusY: 100
//                  }
//                  PathArc {
//                      x: 109; y: 382
//                      radiusX: 100; radiusY: 100
//                  }
//                  PathArc {
//                      x: 188; y: 420
//                      radiusX: 100; radiusY: 100
//                  }
//        }
//    }
}
